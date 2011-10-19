<!SLIDE code code-small>
# "Real life"
    @@@ python
    @app.route("/")
    def public_timeline():
        url = '<twitter_public_timeline_url>' 
        json_resp = requests.get(url)
        posts = json.loads(json_resp.content)
        return render_template(
                    'public_timeline.html', 
                    posts=posts)


<!SLIDE code code-small>

# Quiz!

    @@@ python
    @app.route("/")
    def public_timeline():
        url = '<twitter_public_timeline_url>' 
        json_resp = requests.get(url)
        posts = json.loads(json_resp.content)
        return render_template(
                    'public_timeline.html', 
                    posts=posts)

__Was ist falsch?__


<!SLIDE bullets incremental>

# Böse, weil ...

* Uptime
* Performance
* Testbarkeit

![](devil.jpg)


<!SLIDE bullets incremental>

# Böse, weil ...

* Versionierung
* Deprecation
* Roadmap

![](devil.jpg)

.notes What about FBML? Google turning off APIs?

