from flask import Flask, request

app = Flask(__name__)


@app.route('/')
@app.route('/query')
def query():
    name = request.args.get("name")
    city = request.args.get("city")
    if name and city:
        text = f"Hi, {name}. You are from {city}."
    else:
        text = ""
    return f"<h1>{text}</h1>"


