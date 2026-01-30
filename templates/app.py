from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # host='0.0.0.0' 讓雲端環境能順利轉發網址
    app.run(host='0.0.0.0', port=5000, debug=True)
