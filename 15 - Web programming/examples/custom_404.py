from flask import Flask, request, make_response, render_template

app = Flask(__name__)

@app.route("/")
def home():
    if 'user' in request.headers:
        user = request.headers['user']
        return make_response(f"Hi, {user}", 200)
    return make_response("Hi, Guest", 200)

@app.errorhandler(404)
def page_not_found(e):
    return make_response(render_template('custom_404.html'), 404)
