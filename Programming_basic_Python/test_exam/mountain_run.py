from math import floor
record_sec = float(input())
distance_m = float(input())
speed_m = float(input())
slowing_s = floor(distance_m / 50) * 30
time_sec = distance_m * speed_m + slowing_s
diff = abs(record_sec - time_sec)
if time_sec < record_sec:
    print(f" Yes! The new record is {time_sec:.2f} seconds.")
else:
    print(f"No! He was {diff:.2f} seconds slower.")