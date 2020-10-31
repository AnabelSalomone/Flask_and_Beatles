from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route("/")
def beatles():
    json_file = "data.json"
    with open(json_file) as f:
        json_data = json.load(f)
    return render_template("beatles.html", content = json_data)

@app.route('/songs/<id>')
def songs(id):
    json_file = "data.json"
    with open(json_file) as f:
        json_data = json.load(f)

    for obj in json_data:
        if obj["id"] == int(id):
            return render_template("songs.html", content=obj["tracks"])
        
    return "No data found"

if __name__ == "__main__":
    app.run(debug=True)