n = int(input("Enter a first value: "))
m = int(input("Enter Second value: "))
if n<m:
    print("Second value is greater")
else:
    if n>m:
        print("First value is greater")
    elif n==m:
        print("Both values are equal")
    elif not (isinstance(n, int) and isinstance(m, int)):
     print("Invalid input, please enter numeric values.")