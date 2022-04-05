fruit = input()
week_day = input()
num = float(input())

total = 0

if week_day == "Monday" or week_day == "Tuesday" or week_day == "Wednesday" or week_day == "Thursday" or \
        week_day == "Friday":
    if fruit == "banana":
        total = 2.50 * num
        print(f"{total:.2f}")
    elif fruit == "apple":
        total = 1.20 * num
        print(f"{total:.2f}")
    elif fruit == "orange":
        total = 0.85 * num
        print(f"{total:.2f}")
    elif fruit == "grapefruit":
        total = 1.45 * num
        print(f"{total:.2f}")
    elif fruit == "kiwi":
        total = 2.70 * num
        print(f"{total:.2f}")
    elif fruit == "pineapple":
        total = 5.50 * num
        print(f"{total:.2f}")
    elif fruit == "grapes":
        total = 3.85 * num
        print(f"{total:.2f}")
    else:
        print("error")
elif week_day == "Saturday" or week_day == "Sunday":
    if fruit == "banana":
        total = 2.70 * num
        print(f"{total:.2f}")
    elif fruit == "apple":
        total = 1.25 * num
        print(f"{total:.2f}")
    elif fruit == "orange":
        total = 0.90 * num
        print(f"{total:.2f}")
    elif fruit == "grapefruit":
        total = 1.60 * num
        print(f"{total:.2f}")
    elif fruit == "kiwi":
        total = 3.00 * num
        print(f"{total:.2f}")
    elif fruit == "pineapple":
        total = 5.60 * num
        print(f"{total:.2f}")
    elif fruit == "grapes":
        total = 4.20 * num
        print(f"{total:.2f}")
    else:
        print("error")
else:
    print("error")

















