def generate_vector(idx, vector):
    if idx == len(vector):
        # print(''.join(str(x) for x in vector))
        print(*vector, sep='')
        return
    for num in range(0, 2):
        vector[idx] = num
        generate_vector(idx + 1, vector)


n = int(input())
ll = [None] * n
generate_vector(0, ll)