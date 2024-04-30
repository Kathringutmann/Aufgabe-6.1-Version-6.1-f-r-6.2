virtuelle Umgebung aktivieren: -> über Suchleiste venv ->unten rechts (blau) auf Zahlen -> .venv\Scripts\Activate -> danach pip instal ...

## Erklärung der Änderungen:
# Hinzufügen der put()-Methode
 in der Klasse Person. Diese Methode sendet einen POST-Befehl an den Webserver, um eine neue Person basierend auf dem aktuellen Person-Objekt anzulegen. Dabei wird nur der Vorname verwendet.
# Hinzufügen des email-Attributs
 in der Klasse Subject. Dieses Attribut speichert die E-Mail-Adresse der Person.
# Hinzufügen der update_email()-Methode 
in der Klasse Subject. Diese Methode sendet einen PUT-Befehl an den Webserver, um die E-Mail-Adresse einer Person zu aktualisieren. Dabei wird vorausgesetzt, dass zuvor ein Subject-Objekt mit dem gleichen Vornamen angelegt wurde.
# Beispielhafte Verwendung der neuen Methoden:
Erstellen eines Person-Objekts und Aufruf der put()-Methode, um eine neue Person auf dem Webserver anzulegen.
Erstellen eines Subject-Objekts und Aufruf der update_email()-Methode, um die E-Mail-Adresse auf dem Webserver zu aktualisieren.

# Test.py
In diesem Skript werden die folgenden Schritte durchgeführt:

1.Ein Supervisor-Objekt und ein Subject-Objekt werden erstellt.
2.Ein Experiment-Objekt wird mit dem Supervisor und dem Subject erstellt.
3.Die Details des Experiments werden als Dictionary ausgegeben.
4.Die put()-Methode wird verwendet, um eine neue Person auf dem Webserver anzulegen.
5.Die update_email()-Methode wird verwendet, um die E-Mail-Adresse einer Person auf dem Webserver zu aktualisieren.
6.Das Experiment-Objekt wird in einer JSON-Datei gespeichert.