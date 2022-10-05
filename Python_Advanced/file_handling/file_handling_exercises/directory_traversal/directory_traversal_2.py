import os

dict_files = {}
starting_folder = '../'
for _, _, files in os.walk(starting_folder):
    for elements in files:
        extension = elements.split('.')[-1]
        if extension not in dict_files:
            dict_files[extension] = []
        dict_files[extension].append(elements)
with open("report.txt", 'w') as file:
    for key, val in sorted(dict_files.items(), key=lambda x: x[0]):
        file.write(f".{key}\n")
        for el in sorted(val):
            file.write(f'- - - {el}\n')
