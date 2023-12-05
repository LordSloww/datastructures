# create an empty array to store the numbers
numbers = []

# use a loop to read 6 numbers from the user input
for i in range(6):
    # prompt the user to enter a number
    num = float(input(f"Enter number {i+1}: "))
    # append the number to the array
    numbers.append(num)

# print a blank line for readability
print()

# use another loop to output the numbers in reverse order
print("The numbers in reverse order are:")
for i in range(5, -1, -1):
    # print the number at index i
    print(numbers[i])

# print another blank line for readability
print()

# use the sum() and len() functions to calculate the total and average of the numbers
total = sum(numbers)
average = total / len(numbers)

# print the total and average with two decimal places
print(f"The total of the numbers is: {total:.2f}")
print(f"The average of the numbers is: {average:.2f}")