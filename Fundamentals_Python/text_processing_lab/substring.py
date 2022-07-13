word = input()
input_string = input()
# while True:
#     if word not in input_string:
#         break
#     else:
#         input_string = input_string.replace(word, '')
while word in input_string:
    input_string = input_string.replace(word, '')
print(input_string)
