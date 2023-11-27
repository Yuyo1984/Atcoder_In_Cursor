# TODO edit this code

# param
N = int(input())
A = [*map(int, input().split())]
B = [*map(int, input().split())]

# solve
ans = 0
for i in range(N):
    ans += A[i] * B[i]

# answer
if ans == 0:
    print('Yes')
else:
    print('No')
