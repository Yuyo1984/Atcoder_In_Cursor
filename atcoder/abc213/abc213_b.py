# TODO edit this code

# param
n = int(input())
A = [*map(int, input().split())]

# solve
ans = 0
checker = 0
B = sorted(A)
checker = B[-2]
for i in range(n):
    if A[i] == checker:
        ans = i + 1
        break

# answer
print(ans)
