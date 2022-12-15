def words_(strings_by_index, string_count, strings, target_string):
    for string in strings:
        if string in string_count:
            string_count[string] += 1
            continue
        string_count[string] = 1

        try:
            idx = 0
            while True:
                idx = target_string.index(string, idx)
                if idx not in strings_by_index:
                    strings_by_index[idx] = []
                strings_by_index[idx].append(string)
                idx += len(string)
        except ValueError:
            pass


def find_combinations(idx, target_string, string_count, strings_by_index, used_strings):
    if idx >= len(target_string):
        print(" ".join(used_strings))
        return
    if idx not in strings_by_index:
        return

    for string in strings_by_index[idx]:
        if string_count[string] == 0:
            continue

        used_strings.append(string)
        string_count[string] -= 1
        find_combinations(idx + len(string), target_string, string_count, strings_by_index, used_strings)

        used_strings.pop()
        string_count[string] += 1


strings = input().split(', ')
target_string = input()
strings_by_index = {}
string_count = {}

words_(strings_by_index, string_count, strings, target_string)
find_combinations(0, target_string, string_count, strings_by_index, [])
