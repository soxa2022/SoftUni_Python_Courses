holidays = int(input())
work_days = 365 - holidays
play_time = holidays * 127 + work_days * 63
diff = abs(30000 - play_time)
hours = diff // 60
minutes = diff % 60
if play_time > 30000 :
    print("Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")
else:
    print("Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")

