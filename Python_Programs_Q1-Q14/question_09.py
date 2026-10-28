# Program to build a shopping list
products = ["milk", "bread", "eggs"]
print("Current list:", products)

for i in range(3):
    item = input("Enter a new product " + str(i + 1) + ": ")
    products.append(item)

print("Updated shopping list:", products)
print("Total number of products:", len(products))
