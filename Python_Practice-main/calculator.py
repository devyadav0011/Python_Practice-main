m = int(input("Enter First Digit: "))
n = (input("Enter Symbol: "))
o = int(input("Enter Second value: "))
if n== "+" :
    print(m+o)
else:
    if n == "-":
        print(m-o)
    elif n == "*":
        print(m*o)
    elif n == "/":
        print(m/o)