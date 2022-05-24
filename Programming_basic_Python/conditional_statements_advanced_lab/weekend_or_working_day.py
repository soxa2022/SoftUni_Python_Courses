days = input()
if days == "Monday" or days == "Tuesday" or days == "Wednesday" or days == "Thursday" or days == "Friday":
    print("Working day")
elif days == "Saturday" or days == "Sunday":
    print("Weekend")
else:
    print("Error")