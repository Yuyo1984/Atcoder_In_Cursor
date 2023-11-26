# TODO edit this code

# param
a, b, c = map(int, input().split())

# solve
flag = False
if (a**2 + b**2 < c**2):
    flag = True

# answer
if flag:
    print('Yes')
else:
    print('No')
