electrons = int(input())
count_iter = 0
lst_shells = list()
while electrons != 0:
    count_iter += 1
    electrons_on_shell = 2 * count_iter**2
    if electrons >= electrons_on_shell:
        lst_shells.append(electrons_on_shell)
        electrons -= electrons_on_shell
    else:
        lst_shells.append(electrons)
        electrons = 0
print(lst_shells)