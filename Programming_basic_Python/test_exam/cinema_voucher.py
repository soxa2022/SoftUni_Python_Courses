voucher_price = int(input())
count_tickets = 0
count_other_buy = 0
total_price = voucher_price
buy = input()
while buy != "End":
    price_buy = 0
    if len(buy) > 8:
        price_buy = ord(buy[0]) + ord(buy[1])
        if total_price >= price_buy:
            count_tickets += 1
            total_price -= price_buy
        else:
            break
    else:
        price_buy = ord(buy[0])
        if total_price >= price_buy:
            count_other_buy += 1
            total_price -= price_buy
        else:
            break
    buy = input()
print(f"{count_tickets}")
print(f"{count_other_buy}")
