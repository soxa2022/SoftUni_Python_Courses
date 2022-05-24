from math import floor
needed_processors = int(input())
count_workers = int(input())
work_days = int(input())
time_for_production = work_days * 8
total_time = count_workers * time_for_production
count_produce_processors = floor(total_time / 3)
plan_profit = needed_processors * 110.10
real_profit = count_produce_processors * 110.10
diff = abs(plan_profit - real_profit)
if real_profit >= plan_profit:
    print(f"Profit: -> {diff:.2f} BGN")
else:
    print(f"Losses: -> {diff:.2f} BGN")




