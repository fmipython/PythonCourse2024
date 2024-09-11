from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html', title='Home', user='Lyubo')


@app.route("/login")
def login():
    return render_template('login.html', title='Login')


@app.route("/user/<username>")
def user_page(username):
    return render_template('index.html', title='User', user=username)