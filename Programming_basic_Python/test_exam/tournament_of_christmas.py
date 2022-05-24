count_days = int(input())
total_sum = 0
total_win = 0
total_lose = 0
for i in range(1, count_days + 1):
    type_sport = input()
    count_win = 0
    count_lost = 0
    sum_money = 0
    while type_sport != "Finish":
        result = input()
        if result == "win":
            sum_money += 20
            count_win += 1
            total_win += 1
        elif result == "lose":
            count_lost += 1
            total_lose += 1
        type_sport = input()
    if count_win > count_lost:
        sum_money = sum_money * 1.10
    total_sum += sum_money
if total_win > total_lose:
    total_sum = total_sum * 1.20
    print(f"You won the tournament! Total raised money: {total_sum:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_sum:.2f}")
