# Program to display only the even numbers from ten user inputs
numbers = []

for i in range(10):
    value = int(input("Enter number " + str(i + 1) + ": "))
    numbers.append(value)

print("Even numbers in the list:")
for number in numbers:
    if number % 2 == 0:
        print(number)
