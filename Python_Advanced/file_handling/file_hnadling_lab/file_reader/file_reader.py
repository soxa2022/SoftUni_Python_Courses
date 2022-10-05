path_file = 'numbers.txt'
with open(path_file, 'r') as file:
    nums = file.readlines()
    print(sum([int(s) for s in nums]))
    # nums = file.read()
    # print(sum([int(s) for s in nums.split()]))
