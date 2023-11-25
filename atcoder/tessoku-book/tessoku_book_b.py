n, x = map(int, input().split())
a = [*map(int, input().split())]

flag = False
for i in range(n):
    if a[i] == x:
        flag = True
        break
    
if flag:
    print('Yes')
else:
    print('No')