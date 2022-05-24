count_eggs = int(input())
command_line = input()
sold_eggs = 0
is_closed = True
while command_line != "Close":
    eggs = int(input())
    if command_line == "Buy":
        count_eggs = count_eggs - eggs
        if count_eggs < 0:
            count_eggs = count_eggs + eggs
            is_closed = False
            print(f"Not enough eggs in store!")
            print(f"You can buy only {count_eggs}.")
            break
        else:
            sold_eggs += eggs
    if command_line == "Fill":
        count_eggs += eggs
    command_line = input()
if is_closed:
    print("Store is closed!")
    print(f"{sold_eggs} eggs sold.")
