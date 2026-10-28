# Program to analyse product prices
products = {
    "Laptop": 85000,
    "Mouse": 1200,
    "Keyboard": 2500,
    "Monitor": 18000,
    "Headphones": 3500
}

total = 0
most_expensive = ""
highest_price = 0

print("Products and prices:")
for name in products:
    price = products[name]
    print(name, ": Rs.", price)
    total += price

    if price > highest_price:
        highest_price = price
        most_expensive = name

print("Total price: Rs.", total)
print("Most expensive product:", most_expensive, "(Rs.", highest_price, ")")
