file_name = input("Enter file name: ")
file_handle = open(file_name, "r")
count = 0
total = 0
for line in file_handle:
    if line.startswith("X-DSPAM-Confidence: "):
        new_line = line.replace(" ", "")
        s_pos = new_line.find(":")
        num = float(new_line[s_pos+1:])
        count = count + 1
        total = total + num
average = total / count
print("Average:", average)