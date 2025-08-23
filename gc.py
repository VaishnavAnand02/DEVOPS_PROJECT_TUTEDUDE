mark = int(input("Enter your marks out of 100\n"))
if mark>=0 and mark<=100:
    if mark >=90:
        print("A")
    elif mark>=80 and mark<=89:
        print("B")
    elif mark>=70 and mark<=79:
        print("C")
    elif mark>=60 and mark<=69:
        print("D")
    else:
        print("F")
else:
    print("mark out of range")