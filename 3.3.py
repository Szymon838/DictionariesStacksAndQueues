import queue

expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}" 
expression2 = "[(2+3]/4)"                
expression3 = "(2-3*4+(5/6)"             
def brackets_ok(expression):
    stack = queue.LifoQueue()

    bracket_pairs = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char not in bracket_pairs and char not in bracket_pairs.values():
            continue

        if char in bracket_pairs.values():
            stack.put(char)
        
        elif char in bracket_pairs:
            if stack.empty():
                return False  
            top = stack.get()
            if top != bracket_pairs[char]:
                return False  

    return stack.empty()

if brackets_ok(expression1):
    print("Expression 1: Brackets are correct.")
else:
    print("Expression 1: Brackets are not correct.")

if brackets_ok(expression2):
    print("Expression 2: Brackets are correct.")
else:
    print("Expression 2: Brackets are not correct.")

if brackets_ok(expression3):
    print("Expression 3: Brackets are correct.")
else:
    print("Expression 3: Brackets are not correct.")