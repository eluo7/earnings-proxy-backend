from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os
# from dotenv import load_dotenv
# load_dotenv(override=True)
# API_KEY = os.getenv("FMP_API_KEY")

app = Flask(__name__)
CORS(app)  # 允许跨域，前端可直接请求

API_KEY = os.environ.get("FMP_API_KEY")  # 推荐用环境变量存储API Key


@app.route('/api/earnings')
def earnings():
    from_date = request.args.get('from')
    to_date = request.args.get('to')
    if not from_date or not to_date:
        return jsonify({"error": "Missing 'from' or 'to' parameter"}), 400
    url = f"https://financialmodelingprep.com/stable/earnings-calendar?from={from_date}&to={to_date}&apikey={API_KEY}"
    resp = requests.get(url)
    return jsonify(resp.json())


@app.route('/')
def home():
    return "Earnings Proxy API is running!"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)