# Program to calculate total, average and result from marks
marks = {
    "Mathematics": 65,
    "Science": 48,
    "English": 52
}

total = sum(marks.values())
average = total / len(marks)

print("Marks:", marks)
print("Total marks:", total)
print("Average marks:", round(average, 2))

if average >= 40:
    print("Result: Pass")
else:
    print("Result: Fail")
