import struct

record_format = 'i20sif'  # Define the format for the record (int, 20-char string, int, float)
record_size = struct.calcsize(record_format)  # Calculate the size of each record

with open('records.bin', 'rb') as file:
    file.seek(0)  # Move to the beginning of the file
    while True:
        data = file.read(record_size)
        if not data:
            break
        # Unpack and process the record as shown in the previous example
        record = struct.unpack(record_format, data)
        # Decode the string and remove null characters
        record = (record[0], record[1].decode('utf-8').strip('\x00'), record[2], record[3])
        print(f"ID: {record[0]}, Name: {record[1]}, Age : {record[2]}, GPA: {record[3]:.2f}")