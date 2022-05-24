count_rolls_paper = int(input())
count_rolls_plat = int(input())
count_glue_lt = float(input())
percent_discount = int(input())
price_rolls_paper = count_rolls_paper * 5.80
price_rolls_plat = count_rolls_plat * 7.20
price_glue = count_glue_lt * 1.20
total_price = price_glue + price_rolls_paper + price_rolls_plat
price = total_price * (100 - percent_discount) / 100
print(f"{price:.3f}")


