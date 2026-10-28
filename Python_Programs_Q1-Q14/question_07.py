# Program to store and display student information using a dictionary
student = {
    "name": "Aarav Sharma",
    "age": 18,
    "class": "Year 1 Software Engineering",
    "grade": "A"
}

print("Student Information")
for key in student:
    print(key.capitalize() + ":", student[key])
