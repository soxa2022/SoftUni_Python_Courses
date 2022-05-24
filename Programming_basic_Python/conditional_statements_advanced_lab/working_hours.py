time = int(input())
day = input()
if 10 <= time <= 18 and day != "Sunday":
    print("open")
elif (10 >= time >= 18) or day != "Sunday":
    print("closed")
elif day == "Sunday":
    print("closed")
