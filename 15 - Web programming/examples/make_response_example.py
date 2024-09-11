from flask import Flask, make_response

app = Flask(__name__)

@app.route("/")
def home():
    return make_response("Hello World!", 200, {"Debug": "Hello World!"})

@app.route("/error")
def error():
    return make_response("Error!", 404, {"Debug": "Error!"})