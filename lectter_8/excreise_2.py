# 1. Creating a dictionary
student = {'name': 'Alice', 'age': 26, 'major': 'Computer Science'}

# 2. Dictionary methods: keys(), values(), items()
print(student.keys())
# Output: dict_keys(['name', 'age', 'major'])

print(student.values())
# Output: dict_values(['Alice', 26, 'Computer Science'])

print(student.items())
# Output: dict_items([('name', 'Alice'), ('age', 26), ('major', 'Computer Science')])

# 3. Using get() method
print(student.get("name"))
# Output: Alice

print(student.get("grade", "Not Found"))
# Output: Not Found

# 4. Using pop() method
major = student.pop("major")
print(major)
# Output: Computer Science

print(student)
# Output: {'name': 'Alice', 'age': 26}

# 5. Using popitem() method (ลบและคืนค่าคู่ key-value ตัวสุดท้าย)
last_item = student.popitem()
print(last_item)
# Output: ('age', 26)

print(student)
# Output: {'name': 'Alice'}

# 6. Using clear() method (ล้างข้อมูลทั้งหมดใน dictionary)
student.clear()
print(student)
# Output: {}