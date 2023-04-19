import json

class Person:
    def __init__(self,name,lastname,age) -> None:
        self.name = name
        self.lastname = lastname
        self.age = age

# persons = [{
#     "name":"Arturs",
#     "last_name":"Olekss",
#     "age":25
# },
# {
#     "name":"Kristiana",
#     "last_name":"Indrike",
#     "age":26
# }]

# with open("Persons.json","w") as f:
#     json.dump({"persons":persons},f)

with open("Persons.json","r") as f:
    persons = json.load(f)
    f.close()

persons_objects = list()
for person in persons["persons"]:
    person_obj = Person(person["name"],person["last_name"],person["age"])
    print(persons)
