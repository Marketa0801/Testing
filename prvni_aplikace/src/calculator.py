#Sčítání
def add(a, b):
    return a + b
#Sčítání s chybou
def add_wrong(a,b):
    return 2*a + b
#Odčítání
def subtract(a, b):
    return a - b
#Násobení
def multiply(a, b):
    return a * b
#Násobení s chybou
def multiply_wrong(a,b):
    return a*b + 1
#Děleneí
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b
