donated_sum = int(input())
counter_objects = 1
counter_trans_card = 0
counter_trans_cash = 0
sum_sales_card = 0
sum_sales_cash = 0
is_collected = False
input_line = input()
while input_line != "End":
    object_price = int(input_line)
    if counter_objects % 2 != 0:
        if object_price <= 100:
            sum_sales_cash += object_price
            counter_trans_cash += 1
            print("Product sold!")
        else:
            print("Error in transaction!")
    else:
        if object_price > 10:
            sum_sales_card += object_price
            counter_trans_card += 1
            print("Product sold!")
        else:
            print("Error in transaction!")
    if donated_sum <= sum_sales_cash + sum_sales_card:
        is_collected = True
        print(f"Average CS: {(sum_sales_cash / counter_trans_cash):.2f}")
        print(f"Average CC: {(sum_sales_card / counter_trans_card):.2f}")
        break
    counter_objects += 1
    input_line = input()
if not is_collected or input_line == "End":
    print("Failed to collect required money for charity.")

