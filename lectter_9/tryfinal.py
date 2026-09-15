try:
    a = float(input("Enter the numerator:"    ))
    b = float(input("Enter the denominator:"))
    result = a / b
    print(f"The result of {a} divided by {b} is {result}")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter numeric values.")
finally:
    print("Execution completed, whether an exception occured or not")

print("End of program")