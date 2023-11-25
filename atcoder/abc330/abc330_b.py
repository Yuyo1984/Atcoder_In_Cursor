N, L, R = map(int, input().split())
A = [*map(int, input().split())]

for i in A:
    if i >= L and i <= R:
        print(i, end=' ')
    elif i <= L:
        print(L, end=' ')
    else:
        print(R, end=' ')