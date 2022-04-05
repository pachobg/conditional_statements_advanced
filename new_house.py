flower = input()
flower_count = int(input())
budget = int(input())

price = 0


if flower == "Roses":
    roses_price = flower_count * 5
    if flower_count > 80:
        discount = roses_price * 0.1
        price = roses_price - discount
    else:
        price = roses_price

elif flower == "Dahlias":
    dahlias_price = flower_count * 3.80
    if flower_count > 90:
        discount = dahlias_price * 0.15
        price = dahlias_price - discount
    else:
        price = dahlias_price

elif flower == "Tulips":
    tulip_price = flower_count * 2.80
    if flower_count > 80:
        discount = tulip_price * 0.15
        price = tulip_price - discount
    else:
        price = tulip_price

elif flower == "Narcissus":
    narcissus_price = flower_count * 3
    if flower_count < 120:
        discount = narcissus_price * 0.15
        price = narcissus_price + discount
    else:
        price = narcissus_price

elif flower == "Gladiolus":
    gladiolus_price = flower_count * 2.50
    if flower_count < 80:
        discount = gladiolus_price * 0.2
        price = gladiolus_price + discount
    else:
        price = gladiolus_price

if budget >= price:
    money_left = budget - price
    print(f"Hey, you have a great garden with {flower_count} {flower} and {money_left:.2f} leva left.")
else:
    money_need = price - budget
    print(f"Not enough money, you need {money_need:.2f} leva more.")
