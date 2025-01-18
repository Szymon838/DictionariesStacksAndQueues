import queue

def convert_to_binary(number):
    stack = queue.LifoQueue()

    while number > 0:
        remainder = number % 2
        stack.put(remainder)
        number = number // 2

    binary_number = ""
    while not stack.empty():
        binary_number += str(stack.get())

    return binary_number

number = 18
print(f"Natural number: {number}")

binary = convert_to_binary(number)
print(f"Binary number: {binary}")