#ask user for file name
file_name = input("Enter file name: ")

#open the file in read format
file_handle = open(file_name, "r")

#loop through the file and look for line that starts with "From "
line_list = list()
for line in file_handle:
    line = line.rstrip()
    if not line.startswith("From "): continue
    #if line starts with "From ", split the line
    words = line.split()
    #print the mail, 1 position in the list and add it to a list
    print(words[1])
    line_list.append(words[1])

#print the total mail count
count = len(line_list)
print("There were", count,"lines in the file with From as the first word")