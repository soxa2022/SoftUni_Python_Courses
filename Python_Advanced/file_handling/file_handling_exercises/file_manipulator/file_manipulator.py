import os.path


def create_func(path):
    open(path, 'w').close()


def add_func(path, content):
    with open(path, 'a') as file:
        file.write(content + '\n')


def replace_func(path, old_content, new_content):
    if os.path.exists(path):

        with open(path, 'r+') as file:
            text = file.read().replace(old_content, new_content)
            # file.seek(0)
            # file.truncate()       '''second variant'''
            # file.write(text)

        with open(path, 'w') as file:
            file.write(text)
    else:
        print("An error occurred")


def delete_func(path):

    if os.path.exists(path):
        os.remove(path)
    else:
        print("An error occurred")


def file_manipulate():
    sep = './'
    while True:
        command = input().split('-')

        if command[0] == 'End':
            break
        action, file_path = command[0], sep + command[1]

        if action == 'Create':
            create_func(file_path)
        elif action == 'Add':
            add_func(file_path, command[2])
        elif action == 'Replace':
            replace_func(file_path, command[2], command[3])
        elif action == 'Delete':
            delete_func(file_path)


file_manipulate()
