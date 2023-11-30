# TODO edit this code

# param
H, W = map(int, input().split())
A = [list(map(int, input().split())) for i in range(H)]

flag = True
for n in range(H-1):
    for m in range(W-1):
        if A[n][m] + A[n+1][m+1] > A[n+1][m] + A[n][m+1]:
            flag = False
            break
    if flag is False:
        break
# answer
if flag:
    print('Yes')
else:
    print('No')
