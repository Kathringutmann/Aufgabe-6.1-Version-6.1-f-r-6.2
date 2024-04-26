import json
from datetime import date
from my_classes import Person, Subject, Supervisor, Experiment

def main():
    # Erstellen Sie ein Supervisor-Objekt
    supervisor = Supervisor(first_name="Bob", last_name="Smith", sex="male", birth_date=date(1970, 1, 1))

    # Erstellen Sie ein Subject-Objekt
    subject = Subject(first_name="John", last_name="Doe", sex="male", birth_date=date(1990, 1, 1), phone_number=123456789, max_hr=180)

    # Erstellen Sie ein Experiment-Objekt
    experiment = Experiment(experiment_name="Leistung", experiment_number=2, date=date(2023, 12, 24), supervisor=supervisor, subject=subject)

    filename = "experiment.json"

    with open(filename, 'w') as outfile:
        json.dump(experiment.to_dict(), outfile, default=json_default)

    print(f"Die Experiment- und Versuchsteilnehmerdaten wurden in der Datei '{filename}' gespeichert.")

def json_default(obj):
    if isinstance(obj, date):
        return obj.isoformat()
    else:
        return obj.__dict__

if __name__ == "__main__":
    main()