n = int(input("Enter Your Marks: "))
if n>=90:
    print("Grade A")
else:
    if n>=75:
        print("Grade B")
    elif n>=50 and n<75:
        print("Grade C")
    elif n<50:
        print("Fail")
