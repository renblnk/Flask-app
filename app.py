from flask import Flask, render

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask on GitHub Codespaces!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)