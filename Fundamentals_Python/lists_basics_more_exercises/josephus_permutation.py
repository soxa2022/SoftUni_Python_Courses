lst_numbers = [number for number in input().split()]
k = int(input())
new_list = []
step = k - 1
index = 0
while True:
    if len(lst_numbers) == 0:
        break
    index = (index + step) % len(lst_numbers)
    num = lst_numbers.pop(index)
    new_list.append(num)
print("[" + ",".join(new_list) + "]")
