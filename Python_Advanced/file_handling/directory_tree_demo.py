from os import listdir
from os.path import join, isdir, abspath


# DFS - Depth-first search
def directory_walk(root_directory):
    def directory_walk_internal(current_directory):
        print(current_directory)
        if not isdir(current_directory):
            return

        contents = sorted([d for d in listdir(current_directory)])

        for content in contents:
            directory_walk_internal(join(current_directory, content))

    return directory_walk_internal(
        abspath(root_directory)
    )


directory_walk('./')



