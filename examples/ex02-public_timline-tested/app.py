from flask import Flask, render_template
import json
import requests


class Timeline:

    def __init__(self, impl=None):
        self.impl = TwitterReader() if impl is None else impl

    def get_public_entries(self):
        return self.impl.get_public_timeline()


class TwitterReader:

    def get_public_timeline(self):
        url = 'https://twitter.com/statuses/public_timeline.json' 
        json_resp = requests.get(url)
        return json.loads(json_resp.content)



app = Flask(__name__)

@app.route("/")
def public_timeline():
    posts = Timeline().get_public_entries()
    return render_template('public_timeline.html', posts=posts)

if __name__ == "__main__":
    app.run(debug=True)
