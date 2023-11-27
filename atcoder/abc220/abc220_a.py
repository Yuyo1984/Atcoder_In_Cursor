# TODO edit this code

# param
a, b, c = map(int, input().split())

# solve
ans = 0
flag = False
for i in range(a, b + 1):
    if i % c == 0:
        flag = True
        ans = i
        break
# answer
if flag:
    print(ans)
else:
    print(-1)
