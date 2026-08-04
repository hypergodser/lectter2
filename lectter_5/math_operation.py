def add (a, b):
    return a + b

def subtract (a, b):
    return a - b
def multiply (a, b):
    return a * b
def divide (a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

import math_operation

result_add = math_operation.add(10, 5) 
result_subtract = math_operation.subtract(10, 5)
result_multiply = math_operation.multiply(10, 5)
result_divide = math_operation.divide(10, 5)    

print("Addition:", result_add)
print("Subtraction:", result_subtract)
print("Multiplication:", result_multiply)
print("Division:", result_divide)
