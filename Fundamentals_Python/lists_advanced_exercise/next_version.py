version = [int(element) for element in input().split(".")]
version[-1] += 1
for idx in range(len(version) - 1, -1, -1):
    if version[idx] > 9:
        version[idx] = 0
        version[idx - 1] += 1

    # if version[idx] != 9:
    #     version[idx] += 1
    #     break
    # else:
    #     version[idx] = 0
    #     continue
# print(".".join((list(map(str, version)))))
print(".".join(str(x) for x in version))


# version = [int(element) for element in input().split(".")]
# version = version[::-1]
# for idx, digit in enumerate(version):
#     if digit != 9:
#         version.pop(idx)
#         digit = digit + 1
#         version.insert(idx, digit)
#         break
#     else:
#         version.pop(idx)
#         digit = 0
#         version.insert(idx, digit)
#         continue
# new_version = list(map(str, version[::-1]))
# print(".".join(new_version))

