import struct

# Calculate record size
record_size = struct.calcsize('i20sif')

# Open the binary file for reading
with open("records.bin", "rb") as file:
    while True:
        data = file.read(record_size)
        if not data:
            break
        
        # Unpack the binary data
        record = struct.unpack('i20sif', data)
        # Decode string and remove null characters (\x00)
        record = (record[0], record[1].decode('utf-8').strip('\x00'), record[2], record[3])
        
        # Display the record
        print(f"ID: {record[0]}, Name: {record[1]}, Age: {record[2]}, GPA: {record[3]:.2f}")