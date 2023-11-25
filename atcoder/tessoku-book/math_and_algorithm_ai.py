N, Q = map(int, input().split())
A = [*map(int, input().split())]
LtoR = []
for i in range(Q):
    LtoR.append(list(map(int, input().split())))

S = [0]
S_d = 0
for j in range(len(A)):
    S_d += A[j]
    S.append(S_d)
    
for k in range(Q):
    x = LtoR[k][1]
    y = LtoR[k][0] - 1
    ans = S[x] - S[y]
    print(ans)