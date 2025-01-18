import json

with open('computer.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

for key, value in data.items():
    print(f"{key}: {value}")