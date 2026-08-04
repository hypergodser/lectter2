counter = 0

def increment_counter():
    global counter  # ใช้ตัวแปร global
    counter += 1

increment_counter()
increment_counter()

print("Counter value:", counter)  # Output: Counter value: 2