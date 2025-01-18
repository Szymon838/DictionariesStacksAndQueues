import json

favorite_book = {
    "title": "Harry Potter and the Sorcerer's Stone",
    "author": "J.K. Rowling",
    "genre": "Fantasy",
    "year_of_release": 1997,
    "main_character": "Harry Potter"
}

file_name = "favourite.json"

with open(file_name, 'w') as file:
    json.dump(favorite_book, file, indent=4)

print("Data has been written to", file_name)