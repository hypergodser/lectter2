import datetime

now = datetime.datetime.now()
print("Current date and time:", now)

date_str = "2024-06-15 14:30:00"
date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
print("Date object:", date_obj)

