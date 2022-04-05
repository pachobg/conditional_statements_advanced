hour = int(input())
week_day = input()

if hour < 10 or hour > 18 or week_day == "Sunday":
    print("closed")
else:
    print("open")
