# Open the numbers.txt file
with open("numbers.txt", "r") as numbers_file:
    # Read the 20 integers from the file
    numbers = [int(line.strip()) for line in numbers_file.readlines()]

# Print the even numbers
print("Even numbers:")
for number in numbers:
    if number % 2 == 0:
        print(number)

# Print the odd numbers
print("Odd numbers:")
for number in numbers:
    if number % 2 != 0:
        print(number)