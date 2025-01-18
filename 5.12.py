def reverse_string(input_string):
    stack = []
    
    for char in input_string:
        stack.append(char)
    
    reversed_string = ""
    while stack:
        reversed_string += stack.pop()
    
    return reversed_string

text = input("Enter the text to reverse: ")
reversed_text = reverse_string(text)
print(f"Reversed text: {reversed_text}")