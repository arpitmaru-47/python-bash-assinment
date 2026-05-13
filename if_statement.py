score = int(input("Enter your marks:\n"))

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'
print("Grade :",grade)
#Used if-elif-else statement to check marks and display grades.