<!SLIDE bullets incremental>

# Uptime

* Was ist betroffen, wenn API down/gestört ist?
* Domino Effekt?

![](clock.jpg)


<!SLIDE bullets incremental>

# Performance

* Was ist betroffen, wenn API down/gestört ist?
* Wird Anwendung nur langsam? Zu langsam?
* Siehe "Uptime"

![](snail.jpg)


<!SLIDE bullets incremental>

# Versioning

* APIs ändern sich
* Use-Cases evtl. nicht mehr unterstützt
* Dauerhafte Pflege notwendig

.notes Ist wie beim Hausbau. Mit dem Kaufen/Bauen ist es nicht zu Ende. Heizung geht kaputt, Dach auch


<!SLIDE bullets incremental>

# Testbarkeit ... 

* ... Unit Tests
* ... Integration Tests
* ... Performance Tests
* ... Load Tests


<!SLIDE code code-small>

# Nochmal!

    @@@ python
    @app.route("/")
    def public_timeline():
        url = '<twitter_public_timeline_url>' 
        json_resp = requests.get(url)
        posts = json.loads(json_resp.content)
        return render_template(
                    'public_timeline.html', 
                    posts=posts)

__In dem kleinen Stück Code stecken soviele Probleme__

.notes Und von Security wollen wir gar nicht erst anfangen