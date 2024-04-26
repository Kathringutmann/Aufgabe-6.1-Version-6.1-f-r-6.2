import json
from datetime import date

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

class Subject(Person):
    def __init__(self, first_name, last_name, sex, birth_date, phone_number=None, max_hr=None):
        super().__init__(first_name, last_name, sex, birth_date)
        self.phone_number = phone_number
        self.max_hr = max_hr

class Supervisor(Person):
    def __init__(self, first_name, last_name, sex, birth_date):
        super().__init__(first_name, last_name, sex, birth_date)

class Experiment:
    def __init__(self, experiment_name, experiment_number, date, supervisor, subject):
        self.experiment_name = experiment_name
        self.experiment_number = experiment_number
        self.date = date
        self.supervisor = supervisor
        self.subject = subject
        self.__dict__ = vars(self)

    def to_dict(self):
        return self.__dict__

    def save(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.__dict__, file)

# Erstellen Sie ein Objekt der Experiment-Klasse
supervisor = Supervisor("Supervisor", "1", "male", date(1980, 1, 1))
subject = Subject("John", "Doe", "male", date(1990, 1, 1), "123456789", 180)
experiment = Experiment("Experiment 1", 1, "2023-04-21", supervisor, subject)

# Rufen Sie die to_dict()-Methode auf dem Objekt auf
print(experiment.to_dict())