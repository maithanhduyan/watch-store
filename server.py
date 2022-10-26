from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    title = 'Socket Demo'
    hello = 'Welcome to Watch Store'
    return render_template('index.html', title=title, hello=hello)
