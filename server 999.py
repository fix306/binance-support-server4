from flask import Flask, request, jsonify
from flask_cors import CORS
import threading

app = Flask(__name__)
CORS(app)

latest_message = {"text": ""}

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    try:
        msg = data['message']['text']
        latest_message["text"] = msg
        print(f"Received from Telegram: {msg}")
    except Exception as e:
        print("Invalid Telegram message:", e)
    return jsonify(success=True)

@app.route('/get-latest', methods=['GET'])
def get_latest():
    return jsonify(latest_message)

@app.route('/clear', methods=['POST'])
def clear():
    latest_message["text"] = ""
    return jsonify(success=True)

def run_server():
    app.run(host="0.0.0.0", port=8080)

if __name__ == '__main__':
    run_server()