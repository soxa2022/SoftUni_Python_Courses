length = int(input())
width = int(input())
number_pieces = length * width
input_line = input()
taken_pieces = 0
while input_line != "STOP":
    taken_pieces = int(input_line)
    number_pieces -= taken_pieces
    if number_pieces < 0:
        print(f"No more cake left! You need {abs(number_pieces)} pieces more.")
        break
    input_line = input()
else:
    print(f"{number_pieces} pieces are left.")
