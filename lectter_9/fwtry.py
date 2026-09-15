def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError as e:
        print("exception:", e)

a, b = map(int, input().split())
print(divide(a, b))
print("End of program")