# TODO edit this code

# param
X, Y = map(int, input().split('.'))

# solve
if Y >= 0 and Y <= 2:
    print(str(X) + '-')
elif Y >= 3 and Y <= 6:
    print(X)
else:
    print(str(X) + '+')
