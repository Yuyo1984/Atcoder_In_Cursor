# ヒント見た
N, K = map(int, input().split())

ans = 0
L = N + 1
for i in range(1, L):
    for j in range(1, L):
        W = K - i - j
        if W <= N and W > 0:
            ans += 1
            
# answer
print(ans)
