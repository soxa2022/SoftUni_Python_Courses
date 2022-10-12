from pyfiglet import figlet_format


def print_art(text):
    format_text = figlet_format(text)
    print(format_text)


print_art(input())
