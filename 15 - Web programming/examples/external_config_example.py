from flask import Flask, make_response

app = Flask(__name__)
app.config.from_envvar('FLASK_CONFIG')

@app.route("/")
def home():
    return make_response("Hello World!", 200, {"Debug": "Hello World!"})

if app.config['ENV'] == 'development':
    @app.route("/dev")
    def dev():
        return make_response("This is the development panel !", 200)
