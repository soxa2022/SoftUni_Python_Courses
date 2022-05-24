town = input()
sales = float(input())
percent_commission = 0
commission = 0
if town == "Sofia":
    if 0 <= sales <= 500:
        percent_commission = 5
    elif 500 < sales <= 1000:
        percent_commission = 7
    elif 1000 < sales <= 10000:
        percent_commission = 8
    elif sales > 10000:
        percent_commission = 12
    if sales < 0:
        print("error")
    else:
        commission = sales * (percent_commission / 100)
        print(f"{commission:.2f}")
elif town == "Varna":
    if 0 <= sales <= 500:
        percent_commission = 4.5
    elif 500 < sales <= 1000:
        percent_commission = 7.5
    elif 1000 < sales <= 10000:
        percent_commission = 10
    elif sales > 10000:
        percent_commission = 13
    if sales < 0:
        print("error")
    else:
        commission = sales * (percent_commission / 100)
        print(f"{commission:.2f}")
elif town == "Plovdiv":
    if 0 <= sales <= 500:
        percent_commission = 5.5
    elif 500 < sales <= 1000:
        percent_commission = 8
    elif 1000 < sales <= 10000:
        percent_commission = 12
    elif sales > 10000:
        percent_commission = 14.5
    if sales < 0:
        print("error")
    else:
        commission = sales * (percent_commission / 100)
        print(f"{commission:.2f}")
else:
    print("error")