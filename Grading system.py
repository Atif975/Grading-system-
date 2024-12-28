marks= int(input("Enter your marks "))
if marks>=90:
    print("Your grade is A")
    grade="A"
elif marks>=80 and marks<90:
    print("Your grade is B")
    grade="B"
elif marks>=70 and marks<80:
    print("Your grade is C")
    grade="C"
elif marks>=60 and marks<70:
    print("Your grade is D")
    grade="D"
else:
    print("Your grade is F")
    grade="F"

if marks==100 and grade=="A":
    print ("Perfect Score")
elif marks<40 and grade=="F":
    print("Need serious Improvement!")

    