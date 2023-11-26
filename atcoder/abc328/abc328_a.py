# param
N, X = map(int, input().split())
S = [*map(int, input().split())]
# s = input()

# solve
ans = 0
for i in range(N):
    if S[i] <= X:
        ans += S[i]

# answer
print("{}".format(ans))
