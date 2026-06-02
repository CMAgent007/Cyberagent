def calculate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b != 0:
            return a / b
        else:
            return "Error"

print(calculate(4, 2, '+'))  # Output: 6
print(calculate(4.5, 2, '-'))  # Output: 2.5
print(calculate(4, 2, '*'))  # Output: 8
print(calculate(4, 0, '/'))  # Output: Error