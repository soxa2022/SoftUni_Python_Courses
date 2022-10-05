from os import path

file_path = 'text.txt'
try:
    open(file_path,'r')
    print('File found')
except FileNotFoundError:
    print('File not found')

# if path.exists(file_path):
#     print('File found')
# else:
#     print('File not found')