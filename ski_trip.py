days = int(input())
room_type = input()
judge = input()

price = 0

if room_type == "room for one person":
    price = (days - 1) * 18
elif room_type == "apartment":
    price = (days - 1) * 25
    if days < 10:
        price *= 0.70
    elif 10 <= days <= 15:
        price *= 0.65
    elif days > 15:
        price *= 0.50
elif room_type == "president apartment":
    price = (days - 1) * 35
    if days < 10:
        price *= 0.90
    elif 10 <= days <= 15:
        price *= 0.85
    elif days > 15:
        price *= 0.80

if judge == "positive":
    price = price + (price * 0.25)
elif judge == "negative":
    price = price - (price * 0.1)

print(f"{price:.2f}")
