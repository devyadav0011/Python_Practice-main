n = int(input("Enter first value: "))
m = int(input("Enter second value: "))
o = int(input("Enter third value: "))
if n>m and n>o:
    print("First value is the largest")
else:
    if m>n and m>o:
        print("Second value is the largest")
    elif o>n and o>m:
        print("Third value is the largest")
    elif n==m and n>o:
        print("First and Second values are equal and largest")
    elif n==o and n>m:
        print("First and Third values are equal and largest")
    elif m==o and m>n:
        print("Second and Third values are equal and largest")
    elif n==m and n==o:
        print("All three values are equal")
