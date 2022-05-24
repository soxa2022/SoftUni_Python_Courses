count_chrysanthemums = int(input())
count_roses = int(input())
count_tulips = int(input())
season = input()
holiday = input()
price_bouquet = 0
if season == "Spring" or season == "Summer":
    price_bouquet = count_chrysanthemums * 2 + count_roses * 4.10 + count_tulips * 2.50
    if holiday == "Y":
        price_bouquet *= 1.15
        if count_tulips > 7 and season == "Spring":
            price_bouquet *= 0.95
        if count_tulips + count_roses + count_chrysanthemums > 20:
            price_bouquet *= 0.80
        end_sum = price_bouquet + 2
        print(f"{end_sum:.2f}")
    elif holiday == "N":
        if count_tulips > 7 and season == "Spring":
            price_bouquet *= 0.95
        if count_tulips + count_roses + count_chrysanthemums > 20:
            price_bouquet *= 0.80
        end_sum = price_bouquet + 2
        print(f"{end_sum:.2f}")
if season == "Winter" or season == "Autumn":
    price_bouquet = count_chrysanthemums * 3.75 + count_roses * 4.50 + count_tulips * 4.15
    if holiday == "Y":
        price_bouquet *= 1.15
        if count_roses >= 10 and season == "Winter":
            price_bouquet *= 0.90
        if count_tulips + count_roses + count_chrysanthemums > 20:
            price_bouquet *= 0.80
        end_sum = price_bouquet + 2
        print(f"{end_sum:.2f}")
    elif holiday == "N":
        if count_roses >= 10 and season == "Winter":
            price_bouquet *= 0.90
        if count_tulips + count_roses + count_chrysanthemums > 20:
            price_bouquet *= 0.80
        end_sum = price_bouquet + 2
        print(f"{end_sum:.2f}")






