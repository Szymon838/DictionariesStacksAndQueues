import requests
import json

url = "https://api.nbp.pl/api/exchangerates/rates/A/EUR/last/10?format=json"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    with open('euro.json', 'w') as f:
        json.dump(data, f, indent=4)

    print("Data has been saved to euro.json.")
else:
    print("Failed to fetch data from the NBP API.")