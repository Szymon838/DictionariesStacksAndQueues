import queue

stack = queue.LifoQueue()

stack.put(2)
stack.put(3)
stack.put(7)
stack.put(4)
stack.put(1)
stack.put(9)
stack.put(8)

last_two_sum = stack.get() + stack.get()  
print(f"Sum of the last two numbers: {last_two_sum}")

remaining_sum = 0
while not stack.empty():
    remaining_sum += stack.get()

print(f"Sum of the remaining stack elements: {remaining_sum}")