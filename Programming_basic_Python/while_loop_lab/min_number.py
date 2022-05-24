import sys
num = input()
mim_num = sys.maxsize
while num != "Stop":
    num = int(num)
    if num < mim_num:
        mim_num = num
    num = input()
print(mim_num)