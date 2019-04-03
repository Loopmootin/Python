from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route('/')
def showindexpage():
    return "Hello, Flask!"


if __name__ == '__main__':
    app.run('localhost', 5000)