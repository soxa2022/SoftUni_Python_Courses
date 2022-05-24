month = input()
count_night = int(input())
studio = 0
apartment = 0

if month == "May" or month == "October":
    studio = 50
    apartment = 65
    if 7 < count_night < 14 :
        studio *= 0.95
    elif count_night > 14:
        studio *= 0.70
        apartment *= 0.90
elif month == "June" or month == "September":
    studio = 75.20
    apartment = 68.70
    if count_night > 14:
        studio = studio * 0.80
        apartment = apartment * 0.90
elif month == "July" or month == "August":
    studio = 76
    apartment = 77
    if count_night > 14:
        apartment = apartment * 0.90
sum_for_apartment = apartment * count_night
sum_for_studio = studio * count_night
print(f"Apartment: {sum_for_apartment:.2f} lv.")
print(f"Studio: {sum_for_studio:.2f} lv.")
