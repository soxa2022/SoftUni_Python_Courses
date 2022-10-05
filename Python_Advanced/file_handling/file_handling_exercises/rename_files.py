import os.path
from os import listdir, sep, rename


def rename_file(directory, old_chars, new_chars):
    for name in listdir(directory):
        file = os.path.join(directory, name)

        if os.path.isfile(name):
            new_name = file.split(sep)[-1].replace(old_chars, new_chars)
            new_file = os.path.join(directory, new_name)
            rename(file, new_file)


file_dir = input()
chars_for_replace = input()
replace_with_chars = input()
rename_file(file_dir, chars_for_replace, replace_with_chars)
