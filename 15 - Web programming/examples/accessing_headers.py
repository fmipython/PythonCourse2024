from flask import Flask, request, make_response

app = Flask(__name__)

@app.route("/")
def home():
    if 'user' in request.headers:
        user = request.headers['user']
        return make_response(f"Hi, {user}", 200)
    return make_response("Hi, Guest", 200)