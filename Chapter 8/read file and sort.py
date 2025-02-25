#ask user for file name
file_name = input("Enter file name: ")

#open the file in read format
file_handle = open(file_name, "r")

#loop throught the file and split the lines into lists
line_list = list()
for line in file_handle:
    words = line.split()
    #loop through the list of words and add it to the main list if it is not in the main list
    for word in words:
        if word not in line_list:
            line_list.append(word)
            
#sort and print the sorted list
line_list.sort()
print(line_list)