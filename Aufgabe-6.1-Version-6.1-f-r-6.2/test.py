from datetime import date
from experiment_classes import Supervisor, Subject, Experiment
from config import PERSON_API_URL

# Erstellen eines Supervisor-Objekts
supervisor = Supervisor("Supervisor", "1", "male", date(1980, 1, 1))

# Erstellen eines Subject-Objekts
subject = Subject("John", "Doe", "male", date(1990, 1, 1), "123456789", 180, "john.doe@example.com")

# Erstellen eines Experiment-Objekts
experiment = Experiment("Experiment 1", 1, "2023-04-21", supervisor, subject)

# Ausgabe der Experiment-Details als Dictionary
print(experiment.to_dict())

# Testen der put()-Methode, um eine neue Person auf dem Webserver anzulegen
new_person = subject.put()

# Aktualisieren der E-Mail-Adresse einer Person auf dem Webserver
subject.update_email()

# Speichern des Experiment-Objekts in einer JSON-Datei
experiment.save("experiment_data.json")