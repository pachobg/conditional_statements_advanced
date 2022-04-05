month = input()
overnights = int(input())

studio_price = 0
apartment_price = 0

if month == "May" or month == "October":
    studio_price = overnights * 50
    apartment_price = overnights * 65
    if 7 < overnights <= 14:
        studio_price *= 0.95
    elif overnights > 14:
        studio_price *= 0.7
        apartment_price *= 0.9

elif month == "June" or month == "September":
    studio_price = overnights * 75.20
    apartment_price = overnights * 68.70
    if overnights > 14:
        studio_price *= 0.8
        apartment_price *= 0.9

elif month == "July" or month == "August":
    studio_price = overnights * 76
    apartment_price = overnights * 77
    if overnights > 14:
        apartment_price *= 0.9

print(f"Apartment: {apartment_price:.2f} lv.")
print(f"Studio: {studio_price:.2f} lv.")
