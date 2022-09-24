sub_string = input().split('|')
new_list = []
for s in sub_string[::-1]:
    new_list.extend(s.strip().split())
print(*new_list)

# new_list = [s.strip().split() for s in input().split("|")]
# [print(*x, end=' ') for x in new_list[::-1]]
