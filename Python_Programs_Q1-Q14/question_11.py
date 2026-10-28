# Program to look up the capital of a country
capitals = {
    "Nepal": "Kathmandu",
    "India": "New Delhi",
    "Japan": "Tokyo",
    "France": "Paris",
    "Australia": "Canberra"
}

country = input("Enter a country name: ").strip().title()

if country in capitals:
    print("The capital of", country, "is", capitals[country])
else:
    print("Sorry, that country is not in the dictionary.")
