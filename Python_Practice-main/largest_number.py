# Write a Python program that:
# Asks the user to enter 5 numbers.
# Stores them in a list.
# Prints the largest and smallest number from the list.

number = []
for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    number.append(num)

unique_numbers = list(set(number))
unique_numbers.sort()

print("Largest number is:", unique_numbers[-1])
print("Second largest number is:", unique_numbers[-2])
print("Smallest number is:", unique_numbers[0])
