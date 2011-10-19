<!SLIDE bullets incremental>

# Lösung
## Uptime

* Fehler erwarten


<!SLIDE bullets incremental>

# Lösung
## Uptime

![](chaosmonkey-sw.jpg)

.notes Muss ja nicht gleich der Chaos Monkey sein


<!SLIDE bullets incremental>

# Lösung
## Uptime

* Fehler erwarten
   * langsames Netzwerk
   * API down
   * Timeouts
   * Latency matters

.notes Timeouts, Anzahl Netzwerkaufrufe verringern, Latency matters, Fallacies


<!SLIDE bullets incremental>

# Lösung
## Uptime

* Feature Partitioning
* Bereiche definieren, die von API abhängig sind
* _Nur_ diese dürfen down sein, wenn API down ist


<!SLIDE bullets incremental>

# Lösung
## Performance

* Asynchrones abarbeiten von Tasks


<!SLIDE bullets incremental>

# Lösung
## Performance

* Monitoring & Metrics
* <i>Was beeinflusst die API jetzt? Wie genau?</i>


<!SLIDE bullets incremental>

# Lösung
## Performance

* Caching
* ... schafft aber auch neue Probleme
* ... "only two hard problems in Computer Science"

.notes von Audience erraten lassen ... mit Gummibärchen belohnen






