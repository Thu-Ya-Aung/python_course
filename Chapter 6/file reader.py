file_name = input("Enter File Name: ")
file_handle = open(file_name)
for file in file_handle:
    file = file.rstrip()
    print(file.upper())