# TODO edit this code

# param
X, Y = map(int, input().split())

# solve
flag = False
if (X < Y and X + 3 > Y) or (X > Y and X < Y + 3):
    flag = True

# answer
if flag:
    print('Yes')
else:
    print('No')
