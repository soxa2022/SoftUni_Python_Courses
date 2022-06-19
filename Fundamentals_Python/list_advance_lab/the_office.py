# employees = input().split(" ")
# factor = int(input())
# # employees = list(map(int, employees))
# employees = list(map(lambda x: int(x) * factor, employees))
# average_happiness = sum(employees) / len(employees)
# new_list = list(filter(lambda y: y >= average_happiness, employees))
# # new_list = [element for element in employees if element >= average_happiness]
# if len(employees) // len(new_list) <= 2:  # if len(new_list) >= len(employees) / 2:
#     print(f"Score: {len(new_list)}/{len(employees)}. Employees are happy!")
# else:
#     print(f"Score: {len(new_list)}/{len(employees)}. Employees are not happy!")

employees = [int(person) for person in input().split(" ")]
factor = int(input())
employees = list(map(lambda x: x * factor, employees))
average_happiness = sum(employees) / len(employees)
new_list = list(filter(lambda y: y >= average_happiness, employees))
if len(employees) / len(new_list) <= 2:
    print(f"Score: {len(new_list)}/{len(employees)}. Employees are happy!")
else:
    print(f"Score: {len(new_list)}/{len(employees)}. Employees are not happy!")