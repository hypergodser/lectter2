try:
    value = int(input("Enter a number:"))
    result = 2 ** value
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
else:
    print(f"Result: {result}")

print("End of program")