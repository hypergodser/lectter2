# 1. การแสดงผลและตัวแปร (Variables & Data Types)
name = "Gemini"  # ข้อความ (String)
age = 20  # จำนวนเต็ม (Integer)
height = 175.5  # ทศนิยม (Float)
is_student = True  # บูลีน (Boolean)

print(f"สวัสดี! ฉันชื่อ {name} อายุ {age} ปี")

# 2. รายการข้อมูล (List & Dictionary)
skills = ["Python", "JavaScript", "SQL"]  # List
skills.append("Git")  # เพิ่มข้อมูล

profile = {"name": name, "level": "Beginner"}  # Dictionary (Key-Value)

# 3. เงื่อนไข (If-Else)
score = 85
if score >= 80:
    print("เกรด A")
elif score >= 50:
    print("ผ่าน")
else:
    print("ไม่ผ่าน")

# 4. ลูปวนซ้ำ (Loops)
# วนลูปตามจำนวนรอบ (for loop)
for skill in skills:
    print(f"- มีทักษะ: {skill}")

# วนลูปตามเงื่อนไข (while loop)
count = 0
while count < 3:
    print(f"รอบที่ {count + 1}")
    count += 1


# 5. ฟังก์ชัน (Functions)
def add_numbers(a, b):
    """ฟังก์ชันสำหรับบวกเลขสองตัว"""
    return a + b


result = add_numbers(10, 5)
print(f"ผลรวมของ 10 + 5 คือ {result}")