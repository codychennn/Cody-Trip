from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # 這裡未來會串接機票 API
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
