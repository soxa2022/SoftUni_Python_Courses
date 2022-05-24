# budget = int(input())
# input_line = input()
# while input_line != "End":
#     price = int(input_line)
#     if budget >= price:
#         budget -= price
#     else:
#         print("You went in overdraft!")
#         break
#     input_line = input()
# else:
#     print("You bought everything needed.")

budget = int(input())
input_line = input()
while input_line != "End":
    price = int(input_line)
    budget -= price
    if budget < 0:
        print("You went in overdraft!")
        break
    input_line = input()
else:
    print("You bought everything needed.")
