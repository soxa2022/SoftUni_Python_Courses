count_juniors = int(input())
count_senior = int(input())
type_of_track = input()
collecting_money = 0
if type_of_track == "trail":
    collecting_money = 5.50 * count_juniors + 7 * count_senior
elif type_of_track == "cross-country":
    collecting_money = 8 * count_juniors + 9.50 * count_senior
    if count_senior + count_juniors >= 50:
        collecting_money = collecting_money * 0.75
elif type_of_track == "downhill":
    collecting_money = 12.25 * count_juniors + 13.75 * count_senior
elif type_of_track == "road":
    collecting_money = 20 * count_juniors + 21.50 * count_senior
collecting_money *= 0.95
print(f"{collecting_money:.2f}")



