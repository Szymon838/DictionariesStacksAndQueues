def evaluate_rpn(expression):
    stack = []
    
    tokens = expression.split()
    
    for token in tokens:
        if token.isdigit():  
            stack.append(int(token))
        elif token in ['+', '-', '*', '/']:  
            b = stack.pop()  
            a = stack.pop()  
            
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a / b)
            
        elif token == '=':  
            if stack:
                return stack[-1]  
            else:
                return "Error: Invalid expression"
    
    return "Error: Invalid expression"

if __name__ == "__main__":
    print("Enter RPN expression:")
    expression = input("Example: 2 3 + = \n")
    
    result = evaluate_rpn(expression)
    print("Result: ", result)