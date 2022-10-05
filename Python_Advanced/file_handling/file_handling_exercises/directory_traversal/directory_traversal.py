from os import listdir
from os.path import isdir, join


def directory_traversal(path_file, result):
    for element in listdir(path_file):
        if isdir(join(path_file, element)):
            directory_traversal(join(path_file, element), result)
        else:
            extension = element.split('.')[-1]
            if extension not in result:
                result[extension] = []
            result[extension].append(element)


dict_files = {}
starting_folder = '..'
directory_traversal(starting_folder, dict_files)
with open("report1.txt", 'w') as file:
    for key, val in sorted(dict_files.items(), key=lambda x: x[0]):
        res = f".{key}\n"
        res += '\n'.join([f'- - - {x}' for x in sorted(val)]) + '\n'
        file.write(res)
