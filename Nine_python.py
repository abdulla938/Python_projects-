vMarks = int(input("Enter a marks :"))

if vMarks >0 and vMarks <=30:
    print(" you failed")
elif vMarks > 30 and vMarks <= 40:
    print(" Your grade is 'E'")
elif vMarks > 40 and vMarks <= 50:
    print(" Your grade is 'D'")
elif vMarks > 50 and vMarks <= 60:
    print(" Your grade is 'C'")
elif vMarks > 60 and vMarks <= 70:
    print(" Your grade is 'C'")
elif vMarks > 70 and vMarks <= 80:
    print(" Your grade is 'B'")
elif vMarks > 80 and vMarks <= 90:
    print(" Your grade is 'A'")
elif vMarks > 90 and vMarks <= 100:
    print(" Your grade is 'A+'")
else:
    print("Invalid number or character")
