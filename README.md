## Alte Version
In der alten Version hatten wir folgende Klassen:
# Person-Klasse:
Attribute: first_name, last_name, sex, age, phone_number, max_hr
Methode: estimate_max_hr()
Methode: save()
# Experiment-Klasse:
Attribute: experiment_name, experiment_number, date, supervisor, subject
Methode: to_dict()
Methode: save()
In der Main-Funktion wurde dann ein Person-Objekt und ein Experiment-Objekt erstellt.
## Neue Version
In der neuen Version haben wir die Klassen wie folgt umstrukturiert:
# Person-Klasse (Basisklasse):
Attribute: first_name, last_name, sex, _birth_date
Eigenschaft: age
Methode: estimate_max_hr()
Methode: save()
# Subject-Klasse (Subklasse von Person):
Attribute: phone_number, max_hr
# Supervisor-Klasse (Subklasse von Person):
Keine zusätzlichen Attribute
# Experiment-Klasse:
Attribute: experiment_name, experiment_number, date, supervisor, subject
Methode: to_dict()
Methode: save()
In der Main-Funktion werden nun Subject- und Supervisor-Objekte erstellt und in der Experiment-Klasse verwendet.

## Warum diese Änderungen?
Die Änderungen wurden vorgenommen, um den Code besser zu strukturieren und die Verantwortlichkeiten der einzelnen Klassen klarer zu trennen.
# Basisklasse Person: 
Durch die Einführung der Basisklasse Person können wir gemeinsame Attribute und Methoden in einer zentralen Stelle definieren. Dies erhöht die Wiederverwendbarkeit und Wartbarkeit des Codes.
# Subklassen Subject und Supervisor: 
Die Subklassen Subject und Supervisor erben von der Basisklasse Person und enthalten nur die für sie spezifischen Attribute. Dadurch wird der Code übersichtlicher und es wird deutlich, welche Eigenschaften für Versuchsteilnehmer und Supervisoren relevant sind.
# Verbesserung der Altersberechnung:
In der neuen Version wird das Geburtsdatum als privates Attribut _birth_date gespeichert. Über eine Eigenschaft age wird das Alter dann berechnet. Dies ist genauer als die vorherige Berechnung über das Alter.