contract_duration = input()
type_of_contract = input()
internet = input()
months_for_payment = int(input())
monthly_tax = 0
if contract_duration == "one":
    if type_of_contract == "Small":
        monthly_tax = 9.98
    elif type_of_contract == "Middle":
        monthly_tax = 18.99
    elif type_of_contract == "Large":
        monthly_tax = 25.98
    elif type_of_contract == "ExtraLarge":  # else:
        monthly_tax = 35.99
elif contract_duration == "two":  # else:
    if type_of_contract == "Small":
        monthly_tax = 8.58
    elif type_of_contract == "Middle":
        monthly_tax = 17.09
    elif type_of_contract == "Large":
        monthly_tax = 23.59
    elif type_of_contract == "ExtraLarge":  # else:
        monthly_tax = 31.79
if internet == "yes":
    if monthly_tax <= 10:
        monthly_tax += 5.50
    elif monthly_tax <= 30:
        monthly_tax += 4.35
    else:
        monthly_tax += 3.85
if contract_duration == "two":
    monthly_tax *= 0.9625
total_sum = months_for_payment * monthly_tax
print(f"{total_sum:.2f} lv.")
