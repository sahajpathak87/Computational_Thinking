# Program to count positive, negative and zero values in a tuple
numbers = (5, -3, 0, 12, -8, 0, 7, -1, 9, -6)

positive = 0
negative = 0
zero = 0

for number in numbers:
    if number > 0:
        positive += 1
    elif number < 0:
        negative += 1
    else:
        zero += 1

print("Tuple:", numbers)
print("Positive numbers:", positive)
print("Negative numbers:", negative)
print("Zeros:", zero)
