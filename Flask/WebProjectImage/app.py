from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route('/')
def showindexpage():
    myfilepath = os.path.join('static', 'images', 'mydrawing.jpg')
    return render_template('index.html', user_image=myfilepath)


if __name__ == '__main__':
    app.run('localhost', 5000)