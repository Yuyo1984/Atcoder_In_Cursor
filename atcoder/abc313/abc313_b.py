# TODO edit this code

# バーチャルコンテストで解いた問題
# 結局最後までエラー吐いてダメだった・・・
# 解説読んだので、下に実装していきます
import sys

n, m = map(int, input().split())
rank = [0 for i in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    rank[b] += 1

ans = -1

for i in range(n):
    if rank[i] == 0:
        if ans != -1:
            print(-1)
            sys.exit()
        else:
            ans = i + 1

print(ans)

# 下記は解説の別解。
'''
n, m = map(int, input().split())
s = set(range(1, n+1))
for i in range(m):
    win, lose = map(int, input().split())
    s.discard(lose)
print(-1 if len(s) != 1 else s.pop())
'''

'''
# param
n, m = map(int, input().split())
strong_list = []
for i in range(m):
    strong_list.append(list(map(int, input().split())))

# solve
stronger = strong_list[0][0]
oppo1 = strong_list[0][1]
sum_of_stronger = len(strong_list)
flag = True
oppo2 = strong_list[1][1]
for i in range(1, sum_of_stronger):
    oppo1 = strong_list[i][1]
    oppo2 = strong_list[i+1][1]
    if oppo1 == oppo2:
        flag = False
        break
    if stronger < oppo1:
        stronger = oppo1
    if oppo1 > oppo2:
        oppo1 = oppo2


# answer
if flag:
    print(stronger)
else:
    print(-1)
'''
