import json
def read_reservations(file_path='reservations.json'):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data['reservations']

def count_rooms(reservations):
    return len(reservations)

def count_paid_reservations(reservations):
    return sum(1 for reservation in reservations if reservation['paid'])

def count_unpaid_reservations(reservations):
    return sum(1 for reservation in reservations if not reservation['paid'])

def total_paid_value(reservations):
    return sum(reservation['nights'] * reservation['price_per_night']
               for reservation in reservations if reservation['paid'])

def total_unpaid_value(reservations):
    return sum(reservation['nights'] * reservation['price_per_night']
               for reservation in reservations if not reservation['paid'])

def display_summary(reservations):
    print(f"Number of rooms: {count_rooms(reservations)}")
    print(f"Number of paid reservations: {count_paid_reservations(reservations)}")
    print(f"Number of unpaid reservations: {count_unpaid_reservations(reservations)}")
    print(f"Total value of paid reservations: {total_paid_value(reservations):.2f}")
    print(f"Total value of unpaid reservations: {total_unpaid_value(reservations):.2f}")

def main():
    reservations = read_reservations()
    display_summary(reservations) 

if __name__ == '__main__':
    main()