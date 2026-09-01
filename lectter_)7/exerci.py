employees = [
    {"name": "Ingrid Virgo", "id": 4587, "dept": "Engineering"},
    {"name": "Julia Rich", "id": 4588, "dept": "Research"},
    {"name": "Greg Young", "id": 4589, "dept": "Marketing"}
]

for emp in employees:
    print(f"Name: {emp['name']}")
    print(f"ID: {emp['id']}")
    print(f"Dept: {emp['dept']}")