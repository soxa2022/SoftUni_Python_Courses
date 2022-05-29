count_balls = int(input())
best_ball = 0
best_time = 0
best_quality = 0
best_weight = 0
for balls in range(count_balls):
    weight = int(input())
    time = int(input())
    quality = int(input())
    value_of_ball = (weight / time) ** quality
    if value_of_ball > best_ball:
        best_ball = value_of_ball
        best_weight = weight
        best_quality = quality
        best_time = time
print(f"{best_weight} : {best_time} = {int(best_ball)} ({best_quality})")
