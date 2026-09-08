# Attendance records for a week (each list represents a day's attendance)
attendance_week = [
    ["Alice", "Bob", "Charlie", "David"],  # Day 1 (แก้ ) เป็น ])
    ["Alice", "Charlie", "David"],         # Day 2
    ["Alice", "Bob", "David"],             # Day 3
    ["Alice", "David", "Eve"],             # Day 4
    ["Bob", "Charlie", "David"]            # Day 5
]

# แปลงข้อมูลของแต่ละวันให้เป็น Set เพื่อให้เรียกใช้ attendance_sets ได้
attendance_sets = [set(day) for day in attendance_week]

# 1. Find the set of students who were present every day.
present_every_day = set.intersection(*attendance_sets)
print("Present every day:", present_every_day)
# Output: {'David'}

# 2. Determine the set of students who were absent at least one day.
all_students = set.union(*attendance_sets)
absent_at_least_one_day = all_students - present_every_day
print("Absent at least one day:", absent_at_least_one_day)
# Output: {'Alice', 'Charlie', 'Bob', 'Eve'}

# 3. Create a list of students who were present on the first day but absent on the last day.
first_day_present = attendance_sets[0]
last_day_present = attendance_sets[-1]
first_day_but_not_last = list(first_day_present - last_day_present)
print("Present on first day but absent on last day:", first_day_but_not_last)
# Output: ['Alice']

# 4. Calculate the total number of unique students who attended at least one day.
unique_students_count = len(all_students)
print("Total unique students:", unique_students_count)
# Output: 5