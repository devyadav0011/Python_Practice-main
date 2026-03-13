# Write a Python program that takes a number from the user and prints the multiplication table of that number (from 1 to 10).
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
    