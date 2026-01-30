from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # 這裡未來會串接機票 API
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search_flights():
    origin = request.form.get('origin')
    destination = request.form.get('destination')
    # 未來這裡會寫 API 抓取邏輯
    return f"正在為您搜尋從 {origin} 到 {destination} 的機票..."

if __name__ == '__main__':
    # 修改這裡：加入 host='0.0.0.0'
    app.run(host='0.0.0.0', port=5000, debug=True)
