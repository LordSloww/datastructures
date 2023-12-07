file = open("homework12task1.txt", "r")
line_count = 0
for line in file:
    line_count += 1
file.close()
print("The number of lines in the file is:", line_count)