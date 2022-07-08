number_commands = int(input())
cars_dict = {}
for _ in range(number_commands):
    command = input().split()
    username = command[1]
    if command[0] == "register":
        plate_number = command[2]
        if username in cars_dict:
            print(f"ERROR: already registered with plate number {plate_number}")
        else:
            cars_dict[username] = plate_number
            print(f"{username} registered {plate_number} successfully")
    elif command[0] == "unregister":
        if username in cars_dict:
            cars_dict.pop(username)
            print(f"{username} unregistered successfully")
        else:
            print(f"ERROR: user {username} not found")
# [print(f"{key} => {value}") for key, value in cars_dict.items()]
for key, val in cars_dict.items():
    print(f"{key} => {val}")