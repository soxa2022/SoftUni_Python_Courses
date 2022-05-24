numbers_sites = int(input())
salary_in = int(input())
salary = salary_in
for i in range(1, numbers_sites + 1):
    website = input()
    if website == "Facebook":
        salary = salary - 150
    elif website == "Instagram":
        salary = salary - 100
    elif website == "Reddit":
        salary = salary - 50
    if salary <= 0:
        break
if salary <= 0:
    print("You have lost your salary.")
else:
    print(f"{salary}")
