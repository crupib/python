# Open the binary file for reading
file_handler = open("test.bin", "rb")
# Read the first three bytes from the binary file
data_byte = file_handler.read(7)
print("Print three characters in each iteration:")
# Iterate the loop to read the remaining part of the file
while data_byte:
    print(data_byte)
    data_byte = file_handler.read(7)
# Read the entire file as a single byte string
with open('test.bin', 'rb') as fh:
    content = fh.read()
print("Print the full content of the binary file:")
print(content)

