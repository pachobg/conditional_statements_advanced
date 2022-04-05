projection = input()
ed = int(input())
column = int(input())

price = 0

if projection == "Premiere":
    seats = ed * column
    price = seats * 12
    print(f"{price:.2f}")

elif projection == "Normal":
    seats = ed * column
    price = seats * 7.50
    print(f"{price:.2f}")

elif projection == "Discount":
    seats = ed * column
    price = seats * 5
    print(f"{price:.2f}")

