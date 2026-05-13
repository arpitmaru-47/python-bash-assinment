students = {
    "Anhisekh": "A",
    "Rahul": "B"
}

# Add new student
students["Aman"] = 'A'

# Update grade
students["Rahul"] = 'A'

# Print all students
for name, grade in students.items():
    print(name, ":", grade)
# Used dictionary opertstion to add, update, and print student grades.