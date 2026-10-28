# Program to remove duplicate numbers from a list
numbers = []

for i in range(10):
    value = int(input("Enter number " + str(i + 1) + ": "))
    numbers.append(value)

unique_numbers = []
for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)

print("Original list:", numbers)
print("List with unique numbers:", unique_numbers)
