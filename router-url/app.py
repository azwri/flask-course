from flask import Flask, jsonify


app = Flask(__name__)



@app.route('/')
def index():
    return f"<h1>Hello World</h1>"

@app.route('/json/<name>/<city>')
def json(name, city):
    values = {"name": name, "city": city}
    return jsonify(values)


if __name__ == "__main__":
    app.run(debug=True)