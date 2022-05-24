length_h_m = float(input())
width_h_m = float(input())
length_h_cm = length_h_m * 100
width_h_cm = width_h_m * 100 - 100
work_places = (width_h_cm // 70) * (length_h_cm // 120)
work_places = work_places - 3
print(work_places)

