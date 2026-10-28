# Program to store five numbers in a list and show the list, sum and average
numbers = []

for i in range(5):
    value = float(input("Enter number " + str(i + 1) + ": "))
    numbers.append(value)

total = sum(numbers)
average = total / len(numbers)

print("List of numbers:", numbers)
print("Sum:", total)
print("Average:", average)
