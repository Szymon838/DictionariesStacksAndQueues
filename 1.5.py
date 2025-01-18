countries = [
    {"name": "Poland", "population": 38000000},
    {"name": "India", "population": 1400000000},
    {"name": "USA", "population": 331000000},
    {"name": "Brazil", "population": 213000000},
    {"name": "Japan", "population": 126000000}
]

print(f"{'COUNTRY':<10} {'POPULATION':<15}")
for country in countries:
    print(f"{country['name']:<10} {country['population']:<15}")