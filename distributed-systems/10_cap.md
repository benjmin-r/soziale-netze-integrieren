<!SLIDE>

![](water-jump.jpg)


<!SLIDE>

# CAP Theorem

![](cap.jpg)


<!SLIDE>

## WTF?


<!SLIDE bullets incremental float-img>

# CAP Theorem
## aka "Brewer's theorem"

![](cap-small.jpg)

* Consistency
* Availability
* Partition Tolerance


.notes Hilft beim Entscheiden was wichtig für die jeweilige Anwendung ist
 // CAP ist seit CLoud ein größeres Thema wurde bekannter geworden // 
 Cloud ermöglicht halt nunmal günstig verteilte Systeme aufzubauen


<!SLIDE bullets cap float-img>

# CAP Theorem
## Wähle Zwei

<script>
$(".cap").bind("showoff:next", function (event) {
  var li = $(event.target).find("li:first")
  if ( li.css('text-decoration') == 'none' ) {
    event.preventDefault();
    li.css( {"text-decoration": 'line-through'} );
  }
});
</script>

![](cap-small.jpg)

* Consistency
* Availability
* Partition Tolerance

