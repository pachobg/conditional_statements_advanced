budget = float(input())
season = input()

destination = ""
trip = ""
price = 0

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        trip = "Camp"
        price = budget * 0.3
    elif season == "winter":
        trip = "Hotel"
        price = budget * 0.7
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        trip = "Camp"
        price = budget * 0.4
    elif season == "winter":
        trip = "Hotel"
        price = budget * 0.8
else:
    destination = "Europe"
    trip = "Hotel"
    price = budget * 0.9

print(f"Somewhere in {destination}")
print(f"{trip} - {price:.2f}")




