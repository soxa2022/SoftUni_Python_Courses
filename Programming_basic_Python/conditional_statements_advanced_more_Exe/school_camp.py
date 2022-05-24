season = input()
type_of_group = input()
count_students = int(input())
count_night = int(input())
sport = ""
price = 0

if season == "Winter":
    if type_of_group == "boys":
        sport = "Judo"
        price = 9.60
    elif type_of_group == "girls":
        sport = "Gymnastics"
        price = 9.60
    elif type_of_group == "mixed":
        sport = "Ski"
        price = 10
elif season == "Spring":
    if type_of_group == "boys":
        sport = "Tennis"
        price = 7.20
    elif type_of_group == "girls":
        sport = "Athletics"
        price = 7.20
    elif type_of_group == "mixed":
        sport = "Cycling"
        price = 9.50
elif season == "Summer":
    if type_of_group == "boys":
        sport = "Football"
        price = 15
    elif type_of_group == "girls":
        sport = "Volleyball"
        price = 15
    elif type_of_group == "mixed":
        sport = "Swimming"
        price = 20
if 10 <= count_students < 20:
    price = price * 0.95
elif 20 <= count_students < 50:
    price *= 0.85
elif count_students >= 50:
    price *= 0.50
total_price = price * count_night * count_students
print(f"{sport} {total_price:.2f} lv.")
