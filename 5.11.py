import json
import os

voting_file = 'voting.json'

if os.path.exists(voting_file):
    with open(voting_file, 'r') as file:
        voting_data = json.load(file)
else:
    voting_data = {}

person_name = input('Name of the person you are voting for: ').strip()

if person_name in voting_data:
    voting_data[person_name] += 1  
else:
    voting_data[person_name] = 1  

with open(voting_file, 'w') as file:
    json.dump(voting_data, file, indent=4)

print(f"Vote recorded for {person_name}.")