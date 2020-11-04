from flask import Flask, render_template, request, redirect
from decouple import config
from googleapiclient.discovery import build
import json

app = Flask(__name__)
SECRET_KEY=config('API_KEY')

youtube = build('youtube', 'v3', developerKey=SECRET_KEY)

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
            return render_template("songs.html", content=obj["tracks"], album=obj["name"])
        
    return "No data found"

@app.route('/video/<query>')
def video(query):
        req = youtube.search().list(
            part="snippet",
            maxResults=1,
            q="Beatles " + query
        )

        response = req.execute()
        video = []

        for search_result in response.get("items", []):
            if search_result["id"]["kind"] == "youtube#video":
                video.append(search_result["id"]["videoId"])

        return render_template("video.html", url=video, song=query)


if __name__ == "__main__":
    app.run(debug=True)