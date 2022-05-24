command_input = input()
while command_input != "Welcome!":
    name = command_input
    if name == "Voldemort":
        print(f"You must not speak of that name!")
        break
    if len(name) < 5:
        print(f"{name} goes to Gryffindor.")
    elif len(name) == 5:
        print(f"{name} goes to Slytherin.")
    elif len(name) == 6:
        print(f"{name} goes to Ravenclaw.")
    elif len(name) > 6:
        print(f"{name} goes to Hufflepuff.")
    command_input = input()
if command_input == "Welcome!":
    print("Welcome to Hogwarts.")



