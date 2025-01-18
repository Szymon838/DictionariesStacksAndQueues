import csv

province_dict = {}

with open('province.csv', mode='r', newline='', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        province_dict[row['Letter']] = row['Name']

province_count = {province: 0 for province in province_dict.values()}

with open('vehicle.txt', mode='r', encoding='utf-8') as file:
    for line in file:
        reg_number = line.strip()
        first_letter = reg_number[0]
        
        if first_letter in province_dict:
            province_name = province_dict[first_letter]
            province_count[province_name] += 1

print("Vehicle count by province:")
for province, count in province_count.items():
    print(f"{province}: {count} vehicles")