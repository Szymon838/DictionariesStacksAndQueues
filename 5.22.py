import json

product = {}

product['name'] = input("Enter the product name: ")
product['price'] = float(input("Enter the product price (real number with two decimal places): "))
paid_input = input("Has the product been paid for? (yes/no): ").strip().lower()

if paid_input == 'yes':
    product['paid'] = True
elif paid_input == 'no':
    product['paid'] = False
else:
    print("Invalid input for payment status. Assuming 'no'.")
    product['paid'] = False

file_name = "product.json"

with open(file_name, 'w') as file:
    json.dump(product, file, indent=4)

print("Product data has been written to", file_name)