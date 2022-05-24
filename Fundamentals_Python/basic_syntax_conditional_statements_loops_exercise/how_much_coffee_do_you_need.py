# command_input = input()
# coffee = 0
# while command_input != "END":
#     if command_input == 'coding' or command_input == 'dog' or command_input == 'cat' or command_input == 'movie':
#         coffee += 1
#     elif command_input == 'CODING' or command_input == 'DOG' or command_input == 'CAT' or command_input == 'MOVIE':
#         coffee += 2
#     command_input = input()
# if coffee > 5:
#     print('You need extra sleep')
# else:
#     print(coffee)

command = ""
coffee = 0
while command.lower() != 'end':
    command = input()
    if command.lower() == "movie" or command.lower() == "cat" or \
            command.lower() == "dog" or command.lower() == "coding":
        if command.islower():
            coffee += 1
        elif command.isupper():  # else
            coffee += 2
if coffee > 5:
    print('You need extra sleep')
else:
    print(coffee)

# command_input = input()
# lower_list = ['coding', 'dog', 'cat', 'movie']
# upper_list = ['CODING', 'DOG', 'CAT', 'MOVIE']
# coffee = 0
# while command_input != "END":
#     if command_input in lower_list:
#         coffee += 1
#     elif command_input in upper_list:
#         coffee += 2
#     command_input = input()
# if coffee > 5:
#     print('You need extra sleep')
# else:
#     print(coffee)
