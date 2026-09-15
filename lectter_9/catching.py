try:
    value = int(input("Enter a number: "))
    result = 10 / value
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print(f"Result: {result}")

print ("End of program")