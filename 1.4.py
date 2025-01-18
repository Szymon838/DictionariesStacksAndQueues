person = {
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming", "excursions"],
    "married": True,
    "phone": {"landline": "123444321", "mobile": "777888999"}
}

print("Name:", person["name"])

print("Hobby:", person["hobby"])

print("\nOriginal Dictionary:")
for key, value in person.items():
    print(f"{key} : {value}")

person["surname"] = "Nowak"

person["married"] = not person["married"]  

person["gender"] = "male"

person["hobby"].append("bicycle")

person["phone"]["work"] = "313131444"

print("\nUpdated Dictionary:")
for key, value in person.items():
    print(f"{key} : {value}")