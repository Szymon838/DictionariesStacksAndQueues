import queue

customer_queue = queue.Queue()

ticket_number = 1

while True:
    print("1. Add a new customer")
    print("2. Serve the next customer")
    print("0. Quit")
    menu = input("Select an option: ")

    if menu == '1':
        customer_queue.put(ticket_number)
        print(f"Customer with ticket number {ticket_number} added to the queue.")
        ticket_number += 1  #
    
    elif menu == '2':
        if not customer_queue.empty():
            served_customer = customer_queue.get()
            print(f"Customer with ticket number {served_customer} is being served.")
        else:
            print("No customers in the queue to serve.")
    
    elif menu == '0':
        print("Exiting the customer service system.")
        break

    else:
        print("Invalid option. Please select 1, 2, or 0.")