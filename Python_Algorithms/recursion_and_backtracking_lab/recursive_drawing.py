def drawing(n):
    if n == 0:
        return
    print("*" * n)
    drawing(n - 1)
    print("#" * n)


drawing(int(5))
drawing(int(input()))
