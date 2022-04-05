product = input()
town = input()
number = float(input())

price = 0

if town == "Sofia":
    if product == "coffee":
        price = number * 0.5
    elif product == "water":
        price = number * 0.8
    elif product == "beer":
        price = number * 1.20
    elif product == "sweets":
        price = number * 1.45
    elif product == "peanuts":
        price = number * 1.60

if town == "Plovdiv":
    if product == "coffee":
        price = number * 0.40
    elif product == "water":
        price = number * 0.70
    elif product == "beer":
        price = number * 1.15
    elif product == "sweets":
        price = number * 1.30
    elif product == "peanuts":
        price = number * 1.50

if town == "Varna":
    if product == "coffee":
        price = number * 0.45
    elif product == "water":
        price = number * 0.70
    elif product == "beer":
        price = number * 1.10
    elif product == "sweets":
        price = number * 1.35
    elif product == "peanuts":
        price = number * 1.55

print(price)




