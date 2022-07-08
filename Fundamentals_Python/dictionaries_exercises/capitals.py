country_names = input().split(", ")
capitals = input().split(", ")
# my_dict = dict((zip(country_names, capitals)))
my_dict = {key: val for key, val in zip(country_names, capitals)}
[print(key, '->', value) for key, value in my_dict.items()]
# for key, val in my_dict.items():
#     print(f"{key} -> {val}")


country_names = input().split(", ")
capitals = input().split(", ")
# result = {country_names[index]: capitals[index] for index in range(len(country_names))}
result = dict(zip(country_names, capitals))
for key, val in result.items():
    print(f"{key} -> {val}")
