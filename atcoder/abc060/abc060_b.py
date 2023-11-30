# TODO edit this code

# param
a, b, c = map(int, input().split())

# solve
flag = False
rem_list = []
checker = a % b
n = 2
x = (a * n) % b
while x != checker:
    x = (a * n) % b
    rem_list.append(x)
    n += 1

for i in rem_list:
    if i == c:
        flag = True
        break

# answer
if flag:
    print('YES')
else:
    print('NO')
