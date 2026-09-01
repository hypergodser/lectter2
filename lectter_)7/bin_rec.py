import struct

# Define a record as a tuple
record = (1, 'John Doe', 20, 3.75)

# Open a binary file for writing
with open("records.bin", "wb") as file:
    # Pack the record into binary format
    data = struct.pack('i20sif', record[0], record[1].encode('utf-8'), record[2], record[3])
    # Write the packed data to the file
    file.write(data)