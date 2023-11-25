#下記は解説のコード
N = int(input())
D = [*map(int, input().split())]

ans = 0
for i in range(1,10):
    # i 月 i 日
    if i <= N and i <= D[i - 1]:
        ans += 1
    # i 月 11*i 日
    if i <= N and 11 * i <= D[i - 1]:
        ans += 1
    # 11*i 月 i 日
    if 11 * i <= N and i <= D[11 * i - 1]:
        ans += 1
    # 11*i 月11*i 日
    if 11 * i <= N and 11 * i <= D[11 * i - 1]:
        ans += 1

print(ans)

#ループを思いついたもののゾロ目の判別がわからなかったので解説見る
#全探索はギリギリ出来そう？

'''N = int(input())
D = list(map(int, input().split()))

M = [x+1 for x in range(N)]
c = 0

for i in range(N):
    for j in range(D[j]):
        D_M = [x+1 for x in range(D[j])]
        day = str(M[i]) + str(D_M[j])'''