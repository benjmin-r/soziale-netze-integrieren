from flask import Flask, render_template
import json
import requests


app = Flask(__name__)

@app.route("/")
def public_timeline():
    url = 'https://twitter.com/statuses/public_timeline.json' 
    json_resp = requests.get(url)
    posts = json.loads(json_resp.content)
    return render_template('public_timeline.html', posts=posts)

if __name__ == "__main__":
    app.run(debug=True)