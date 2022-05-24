fuel = input()
liters = float(input())
if liters >= 25 and fuel == "Diesel":
    print("You have enough diesel.")
elif liters < 25 and fuel == "Diesel":
    print("Fill your tank with diesel!")
elif liters >= 25 and fuel == "Gasoline":
    print("You have enough gasoline.")
elif liters < 25 and fuel == "Gasoline":
    print("Fill your tank with gasoline!")
elif liters >= 25 and fuel == "Gas":
    print("You have enough gas.")
elif liters < 25 and fuel == "Gas":
    print("Fill your tank with gas!")
else:
    print("Invalid fuel!")