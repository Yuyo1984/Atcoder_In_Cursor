# TODO edit this code

# param
n, a, b = map(int, input().split())
s = input()

# solve
x = len(s)
c_n = 0
c_w = 0
sum = a + b
for i in range(x):
    if s[i] == "a" and (c_n + c_w) < sum:
        print('Yes')
        c_n += 1
    elif s[i] == "b" and (c_n + c_w) < sum and c_w < b:
        print('Yes')
        c_w += 1
    else:
        print('No')
