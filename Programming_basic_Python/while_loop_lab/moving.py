width = int(input())
length = int(input())
height = int(input())
volume_apartment = width * length * height
volume_cartons = 0
diff = 0
input_line = input()
while input_line != "Done":
    cartons = int(input_line)
    volume_cartons += cartons
    diff = volume_apartment - volume_cartons
    if diff < 0 :
        print(f"No more free space! You need {abs(diff)} Cubic meters more.")
        break
    input_line = input()
else:
    print(f"{abs(diff)} Cubic meters left.")



