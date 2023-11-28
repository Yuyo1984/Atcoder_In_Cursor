# TODO edit this code

# param
N, P = map(int, input().split())
A = [*map(int, input().split())]

# solve
ans = 0
for n in range(N):
    if A[n] < P:
        ans += 1

# answer
print(ans)
