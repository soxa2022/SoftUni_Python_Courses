key_number = int(input())
count_lines = int(input())
massage = ""
for char in range(count_lines):
    character = ord(input())
    massage += chr(character + key_number)
print(massage)

