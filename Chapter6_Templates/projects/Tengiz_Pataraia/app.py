import flask
import json

app = flask.Flask(__name__)

with open("parts.json","r")as file:
    parts = json.load(file)

@app.route("/")
def index():
    return flask.render_template("about.html")

@app.route("/parts/<part_name>")
def part(part_name):
    data = parts[part_name]
    return flask.render_template("part.html",data=data)

if __name__ == "__main__":
    app.run(debug=True)
