price_list = {
    'T-shirt': 19.99,
    'Jeans': 49.99,
    'Jacket': 89.99,
    'Sneakers': 59.99,
    'Hat': 15.99
}

print(f"{'PRODUCT':<10} {'PRICE (Before Discount)':<10}")
for product, price in price_list.items():
    print(f"{product:<10} ${price:<10.2f}")

total_before_discount = sum(price_list.values())
print("\nTotal value of the products before the discount: $", round(total_before_discount, 2))

for product in price_list:
    price_list[product] = round(price_list[product] * 0.9, 2)

print(f"\n{'PRODUCT':<10} {'PRICE (After Discount)':<10}")
for product, price in price_list.items():
    print(f"{product:<10} ${price:<10.2f}")

total_after_discount = sum(price_list.values())
print("\nTotal value of the products after the discount: $", round(total_after_discount, 2))