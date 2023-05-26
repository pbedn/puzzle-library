from datetime import datetime

CURRENT_DATE = "01.01.2018"


class Person:
    def __init__(
        self,
        first_name,
        last_name,
        birth_date,
        job,
        working_years,
        salary,
        country,
        city,
        gender="unknown",
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.job = job
        self.working_years = working_years
        self.salary = salary
        self.country = country
        self.city = city
        self.gender = gender if gender else "unknown"

    def name(self):
        return self.first_name + " " + self.last_name

    def age(self):
        current_date = datetime.strptime(CURRENT_DATE, "%d.%m.%Y")
        birth_date = datetime.strptime(self.birth_date, "%d.%m.%Y")
        difference = (current_date.month, current_date.day) < (
            birth_date.month,
            birth_date.day,
        )
        return current_date.year - birth_date.year - difference

    def work(self):
        prefix = "Is"
        if self.gender == "female":
            prefix = "She is"
        elif self.gender == "male":
            prefix = "He is"
        return "{} a {}".format(prefix, self.job)

    def money(self):
        salary = str(self.working_years * 12 * self.salary)
        new_format = ""
        for i, l in enumerate(reversed(salary)):
            if i % 3 == 0 and i != 0:
                new_format = " " + new_format
            new_format = l + new_format
        return new_format

    def home(self):
        return "Lives in {}, {}".format(self.city, self.country)


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing

    p1 = Person(
        "John", "Smith", "19.09.1979", "welder", 15, 3600, "Canada", "Vancouver", "male"
    )
    p2 = Person(
        "Hanna Rose", "May", "05.12.1995", "designer", 2.2, 2150, "Austria", "Vienna"
    )
    p3 = Person(
        "Kate", "Hound", "05.02.2000", "student", 0, 0, "Australia", "Sydney", "female"
    )
    p4 = Person(
        "Adam",
        "Greene",
        "24.12.1961",
        "director",
        36,
        11000,
        "England",
        "London",
        "male",
    )
    assert p1.name() == "John Smith", "Name"
    assert p1.age() == 38, "Age"
    assert p2.work() == "Is a designer", "Job"
    assert p1.money() == "648 000", "Money"
    assert p2.home() == "Lives in Vienna, Austria", "Home"
    print("Coding complete? Let's try tests!")
    assert p3.work() == "She is a student"
    assert p4.money() == "4 752 000"
