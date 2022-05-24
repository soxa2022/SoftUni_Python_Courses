type_cat = input()
gender = input()
life_months = 0
is_not_valid = False
if gender == "m":
    if type_cat == "British Shorthair":
        life_months = (13 * 12) / 6
    elif type_cat == "Siamese":
        life_months = (15 * 12) / 6
    elif type_cat == "Persian":
        life_months = (14 * 12) / 6
    elif type_cat == "Ragdoll":
        life_months = (16 * 12) / 6
    elif type_cat == "American Shorthair":
        life_months = (12 * 12) / 6
    elif type_cat == "Siberian":
        life_months = (11 * 12) / 6
    else:
        is_not_valid = True
if gender == "f":
    if type_cat == "British Shorthair":
        life_months = (14 * 12) / 6
    elif type_cat == "Siamese":
        life_months = (16 * 12) / 6
    elif type_cat == "Persian":
        life_months = (15 * 12) / 6
    elif type_cat == "Ragdoll":
        life_months = (17 * 12) / 6
    elif type_cat == "American Shorthair":
        life_months = (13 * 12) / 6
    elif type_cat == "Siberian":
        life_months = (12 * 12) / 6
    else:
        is_not_valid = True
if is_not_valid:
    print(f"{type_cat} is invalid cat!")
else:
    print(f"{round(life_months)} cat months")






    # "British Shorthair", "Siamese", "Persian", "Ragdoll", "American Shorthair"
    # или
    # "Siberian"