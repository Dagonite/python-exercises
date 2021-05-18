# employee_keywords.py
# pylint: disable=no-member
"""Create a class, Employee, that will take a full name as an argument, as well as zero or more keywords. Each instance 
should have name and lastname attributes, plus attributes for each keyword (if any)."""


class Employee:
    def __init__(self, fullname, **kwargs):
        self.name, self.lastname = fullname.split()
        for key, value in kwargs.items():
            setattr(self, key, value)


if __name__ == "__main__":
    adam = Employee("Adam Tabett")
    mary = Employee("Mary Howlette", salary=34000)
    john = Employee("John Rico", salary=65000, height=178)
    lance = Employee("Lance Morales", salary=98000, height=182, nationality="American")

    test_cases = [
        (adam, {"name": "Adam", "lastname": "Tabett"}),
        (mary, {"name": "Mary", "lastname": "Howlette", "salary": 34000}),
        (john, {"name": "John", "lastname": "Rico", "salary": 65000, "height": 178}),
        (lance, {"name": "Lance", "lastname": "Morales", "salary": 98000, "height": 182, "nationality": "American"}),
    ]

    for i, test_case in enumerate(test_cases, start=1):
        person, data = test_case
        print(f"\nTest case: {i}")
        for key, value in data.items():
            attribute = getattr(person, key)
            print("[PASS]" if attribute == value else "[FAIL]", f"{data['name'].lower()}.{key} = {attribute}")