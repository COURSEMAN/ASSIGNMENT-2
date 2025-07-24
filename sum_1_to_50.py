# Program to calculate sum of integers from 1 to 50 using a for loop

# Initialize sum variable
sum_of_numbers = 0

# Use for loop to iterate from 1 to 50
for i in range(1, 51):  # range(1, 51) gives numbers from 1 to 50
    sum_of_numbers += i  # Add each number to the sum

# Display the final result
print(f"The sum of numbers from 1 to 50 is: {sum_of_numbers}")