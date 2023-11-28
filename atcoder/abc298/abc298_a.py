# TODO edit this code

# param
n = int(input())
s = input()
# solve
flag1 = False
flag2 = True
for i in range(n):
    if s[i] == 'o':
        flag1 = True
    if s[i] == 'x':
        flag2 = False
# answer
if flag1 and flag2:
    print('Yes')
else:
    print('No')
