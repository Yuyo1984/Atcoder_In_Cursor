# TODO edit this code

# param
x, y = map(int, input().split('.'))
# solve
ans = 0
if int(str(y)[0]) <= 4:
    ans = x
else:
    ans = x + 1

# answer
print(ans)
