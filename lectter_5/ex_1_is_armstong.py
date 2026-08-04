def is_armstrong(number):
    # 1. แปลงตัวเลขเป็นสตริงเพื่อใช้นับและแยกหลัก
    num_str = str(number)
    
    # 2. หาจำนวนหลักของตัวเลข
    num_digits = len(num_str)
    
    # 3. กำหนดค่าเริ่มต้นของผลรวมเป็น 0
    total = 0
    
    # 4. วนลูปหยิบแต่ละเลขโดดมาเข้าสูตร ยกกำลังด้วยจำนวนหลัก แล้วบวกสะสมใน total
    for digit in num_str:
        total += int(digit) ** num_digits
        
    # 5. ตรวจสอบว่าผลรวมเท่ากับตัวเลขตั้งต้นหรือไม่
    if total == number:
        return True
    else:
        return False

# --- Example usage ---
print(is_armstrong(153))   # Output: True (153 = 1^3 + 5^3 + 3^3)
print(is_armstrong(9474))  # Output: True (9474 = 9^4 + 4^4 + 7^4 + 4^4)
print(is_armstrong(123))   # Output: False (123 is not an Armstrong number)