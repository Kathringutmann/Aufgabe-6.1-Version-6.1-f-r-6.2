import json
from datetime import date
import requests
from config import PERSON_API_URL

class Person:
    def __init__(self, first_name, last_name, sex, birth_date):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self._birth_date = birth_date
        self.__dict__ = vars(self)

    @property
    def age(self):
        today = date.today()
        return today.year - self._birth_date.year - ((today.month, today.day) < (self._birth_date.month, self._birth_date.day))

    def estimate_max_hr(self):
        """
        See https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4124545/ for different formulas
        """
        if self.sex == "male":
            max_hr_bpm = 223 - 0.9 * self.age
        elif self.sex == "female":
            max_hr_bpm = 226 - 1.0 * self.age
        else:
            max_hr_bpm = int(input("Enter maximum heart rate: "))
        return int(max_hr_bpm)

    def save(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.__dict__, file)

    def put(self):
        """
        Legt eine neue Person auf dem Webserver an, basierend auf dem aktuellen Person-Objekt.
        Nur der Vorname wird verwendet.
        """
        url = PERSON_API_URL
        data = {"first_name": self.first_name}
        response = requests.post(url, json=data)
        if response.status_code == 201:
            print(f"Person {self.first_name} erfolgreich angelegt.")
        else:
            print(f"Fehler beim Anlegen der Person {self.first_name}: {response.status_code} - {response.text}")

class Subject(Person):
    def __init__(self, first_name, last_name, sex, birth_date, phone_number=None, max_hr=None, email=None):
        super().__init__(first_name, last_name, sex, birth_date)
        self.phone_number = phone_number
        self.max_hr = max_hr
        self.email = email

    def to_dict(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "sex": self.sex,
            "_birth_date": self._birth_date.strftime("%Y-%m-%d"),
            "phone_number": self.phone_number,
            "max_hr": self.max_hr,
            "email": self.email
        }

    def update_email(self):
        """
        Aktualisiert die E-Mail-Adresse einer Person auf dem Server.
        Setzt voraus, dass zuvor ein Subject mit dem gleichen Vornamen angelegt wurde.
        """
        url = f"{PERSON_API_URL}/{self.first_name}"
        data = {"email": self.email}
        response = requests.put(url, json=data)
        if response.status_code == 200:
            print(f"E-Mail-Adresse von {self.first_name} erfolgreich aktualisiert.")
        else:
            print(f"Fehler beim Aktualisieren der E-Mail-Adresse von {self.first_name}: {response.status_code} - {response.text}")

class Supervisor(Person):
    def __init__(self, first_name, last_name, sex, birth_date):
        super().__init__(first_name, last_name, sex, birth_date)

    def to_dict(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "sex": self.sex,
            "_birth_date": self._birth_date.strftime("%Y-%m-%d")
        }

class Experiment:
    def __init__(self, experiment_name, experiment_number, date, supervisor, subject):
        self.experiment_name = experiment_name
        self.experiment_number = experiment_number
        self.date = date
        self.supervisor = supervisor.to_dict()
        self.subject = subject.to_dict()
        self.__dict__ = vars(self)

    def to_dict(self):
        return self.__dict__

    def save(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.to_dict(), file)