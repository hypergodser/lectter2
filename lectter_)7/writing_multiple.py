import struct

num_records = int(input("How many records do you want to write? "))

with open("records.bin", "wb") as file:
    for i in range(num_records):
        name = input(f"Enter name for record {i + 1}: ")
        age = int(input(f"Enter age for record {i + 1}: "))
        gpa = float(input(f"Enter GPA for record {i + 1}: "))

        # Pack the data into binary format
        data = struct.pack('20sif', name.encode('utf-8'), age, gpa)
        file.write(data)
print(f"{num_records} records written to records.bin.")