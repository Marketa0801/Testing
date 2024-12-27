def add(a, b):
    return a + b

def add_wrong(a,b):
    return 2*a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def multiply_wrong(a,b):
    return a*b + 1

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b
