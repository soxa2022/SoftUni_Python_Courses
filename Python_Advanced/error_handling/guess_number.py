import random
from colorama import Fore


class InvalidLevelInputError(Exception):
    pass


while True:
    try:
        level = int(input(Fore.BLUE + 'Enter the level: '))
        break
    except ValueError:
        print(Fore.RED + "Enter integer number")

if level <= 0:
    raise InvalidLevelInputError(Fore.RED + 'Enter valid number')

computer_number = random.randint(1, 10 * level)

while True:
    try:
        player_number = int(input(Fore.WHITE + "Enter your guess number: "))
    except ValueError:
        print(Fore.RED + 'Enter int number')
        continue

    if player_number == computer_number:
        print(Fore.MAGENTA + "You guessed it")
        if not input(Fore.YELLOW + "Do yu want to play again? [y/n]: ") == 'y':
            break
        level += 1
        computer_number = random.randint(1, 10 * level)
        print(Fore.WHITE + f'Your are in level: {level}')
    elif player_number < computer_number:
        print(Fore.BLUE + "It is bigger")
    else:
        print(Fore.BLUE + 'It is smaller')
