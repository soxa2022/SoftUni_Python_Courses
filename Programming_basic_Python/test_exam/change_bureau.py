count_bitcoin = int(input())
count_chinese_uan = float(input())
commission = float(input())
price_bitcoin_lv = count_bitcoin * 1168
price_chinese_lv = count_chinese_uan * 0.15 * 1.76
total_euros = (price_chinese_lv + price_bitcoin_lv) / 1.95
total_euros = total_euros * (1 - commission / 100)
print(f"{total_euros:.2f}")
