from flask import Flask, request, render_template
from stories import story

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("base.html", story=story.prompts)

@app.route("/story")
def story_page():
    full_story = story.generate(request.args)
    return render_template("story.html", full_story=full_story)