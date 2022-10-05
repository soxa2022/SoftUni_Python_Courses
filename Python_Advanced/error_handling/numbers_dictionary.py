import sys
from io import StringIO

test_input1 = '''one
1
two
2
Search
one
Remove
two
End
'''
test_input2 = '''one
two
Search
Remove
End
'''
test_input3 = '''one
1
Search
one
Remove
two
End
'''

# """ task inputs"""
# sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)
sys.stdin = StringIO(test_input3)

numbers_dictionary = {}

line = input()
while line != "Search":
    number_as_string = line
    try:
        number = int(input())
        numbers_dictionary[number_as_string] = number
    except ValueError:
        print("The variable number must be an integer")
    line = input()

line = input()
while line != "Remove":
    searched = line
    try:
        print(numbers_dictionary[searched])
    except KeyError:
        print("Number does not exist in dictionary")
    line = input()

line = input()
while line != "End":
    searched = line
    try:
        del numbers_dictionary[searched]
    except KeyError:
        print("Number does not exist in dictionary")
    line = input()

print(numbers_dictionary)
