from flask import Flask, render_template
import csv
import json

app = Flask(__name__)

@app.route("/oscar/")
def oscar():
    csv_name = "oscar_age_male.csv"
    data = []
    with open(csv_name) as f:
        reader = csv.reader(f)
        next(f)
        for line in reader:
            data.append(line[3])

    return render_template("oscars.html", content=data)

@app.route("/beatles/")
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
        
    return "coucou"

if __name__ == "__main__":
    app.run(debug=True)