# Program to check if a number is even or odd

# Get input from user
number = int(input("Enter a number: "))

# Check if the number is even or odd using if-else statement
if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")