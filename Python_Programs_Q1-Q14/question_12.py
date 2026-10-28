# Program to manage results of five students
students = {
    "Anil": 72,
    "Bina": 38,
    "Chandra": 55,
    "Deepa": 91,
    "Esha": 40
}

top_name = ""
top_marks = -1

for name in students:
    marks = students[name]

    if marks >= 40:
        result = "Pass"
    else:
        result = "Fail"

    print("Name:", name, "| Marks:", marks, "| Result:", result)

    if marks > top_marks:
        top_marks = marks
        top_name = name

print("Highest marks:", top_name, "with", top_marks)
