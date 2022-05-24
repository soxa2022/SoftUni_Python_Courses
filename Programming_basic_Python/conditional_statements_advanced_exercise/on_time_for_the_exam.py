exam_hour_start = int(input())
exam_minutes_start = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())
arrival_time = arrival_minutes + arrival_hour * 60
exam_time_minutes = exam_minutes_start + exam_hour_start * 60
diff = abs(arrival_time - exam_time_minutes)
hour = diff // 60
minutes = diff % 60
if arrival_time > exam_time_minutes:
    print("Late")
    if diff < 60:
        print(f"{diff} minutes after the start")
    elif diff >= 60 and minutes >= 10:
        print(f"{hour}:{minutes} hours after the start")
    else:
        print(f"{hour}:0{minutes} hours after the start")
elif arrival_minutes <= exam_time_minutes and diff <= 30:
    print("On time")
    if 0 < diff < 60:
        print(f"{diff} minutes before the start")
else:
    print("Early")
    if diff < 60:
        print(f"{diff} minutes before the start")
    elif diff >= 60 and minutes >= 10:
        print(f"{hour}:{minutes} hours before the start")
    else:
        print(f"{hour}:0{minutes} hours before the start")


