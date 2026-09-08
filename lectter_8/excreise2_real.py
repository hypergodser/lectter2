# Sample data structure for employee performance
performance_data = {
    "Sales": {
        "Alice": [80, 85, 88, 90],
        "Bob": [70, 75, 78, 80],
        "Charlie": [60, 65, 70, 72]
    },
    "Engineering": {
        "David": [90, 92, 94, 95],
        "Eve": [85, 88, 87, 90],
        "Frank": [88, 87, 86, 85]
    },
    "HR": {
        "Grace": [70, 72, 74, 76],
        "Heidi": [65, 68, 70, 73],
        "Ivan": [60, 62, 64, 66]
    }
}

# 1. Calculate the average performance score for each employee
average_scores = {}
for department, employees in performance_data.items():
    average_scores[department] = {}
    for employee, scores in employees.items():
        average = sum(scores) / len(scores)
        average_scores[department][employee] = average

# 2. Identify the top performer in each department based on their average score
top_performers = {}
for department, employees in average_scores.items():
    # หาพนักงานที่ได้คะแนนเฉลี่ยสูงสุดในแผนก
    top_employee = max(employees, key=employees.get)
    top_performers[department] = (top_employee, employees[top_employee])

# 3. Determine the department with the highest average performance score
dept_averages = {}
for department, employees in average_scores.items():
    dept_avg = sum(employees.values()) / len(employees)
    dept_averages[department] = dept_avg

best_department_name = max(dept_averages, key=dept_averages.get)
best_department_score = dept_averages[best_department_name]

# 4. Find employees who have shown continuous improvement
# (คะแนนแต่ละรอบต้องเพิ่มขึ้นเรื่อยๆ: score[i] < score[i+1])
continuous_improvers = {}
for department, employees in performance_data.items():
    improvers = []
    for employee, scores in employees.items():
        # ตรวจสอบว่าคะแนนเพิ่มขึ้นต่อเนื่องทุกช่วงหรือไม่
        is_improving = all(scores[i] < scores[i + 1] for i in range(len(scores) - 1))
        if is_improving:
            improvers.append(employee)
    continuous_improvers[department] = improvers

# 5. Generate a summary report
print(f"Average Performance Scores: {average_scores}")
print(f"Top Performers: {top_performers}")
print(f"Best Department: {best_department_name} {best_department_score}")
print(f"Continuous Improvers: {continuous_improvers}")