degrees = int(input())
time_of_the_day = input()
if degrees >= 10 and degrees <= 18:
    if time_of_the_day == "Morning":
        print(f"It's {degrees} degrees, get your Sweatshirt and Sneakers.")
    elif time_of_the_day == "Afternoon" or time_of_the_day == "Evening":
        print(f"It's {degrees} degrees, get your Shirt and Moccasins.")
elif 18 < degrees <= 24: # еднавко като първата проверка
    if time_of_the_day == "Afternoon":
        print(f"It's {degrees} degrees, get your T-Shirt and Sandals.")
    elif time_of_the_day == "Morning" or time_of_the_day == "Evening":
        print(f"It's {degrees} degrees, get your Shirt and Moccasins.")
elif degrees >= 25:
    if time_of_the_day == "Morning":
        print(f"It's {degrees} degrees, get your T-Shirt and Sandals.")
    elif time_of_the_day == "Afternoon":
        print(f"It's {degrees} degrees, get your Swim Suit and Barefoot.")
    elif time_of_the_day == "Evening":
        print(f"It's {degrees} degrees, get your Shirt and Moccasins.")
