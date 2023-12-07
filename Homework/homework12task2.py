input_file = open("homework12task1.txt", "r")
output_file = open("homework12task2.txt", "w")
first_line = input_file.readline()
words = first_line.split()
for word in words:
    output_file.write(word + "\n")
input_file.close()
output_file.close()