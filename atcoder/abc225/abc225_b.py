import sys

n = int(input())
count = [0 for i in range(n)]
for j in range(1, n):
    a, b = map(int, input().split())
    count[a-1] += 1
    count[b-1] += 1

for k in range(0, n):
    if count[k] == n-1:
        print('Yes')
        sys.exit()

print('No')
# 10分考えてギブアップ。全部まとめて一つのリストを作った後、一番多い要素を抽出して、その個数が全体の半分ぴったりならOK
# ってやりたかったけど、その方法が思いつかなかった
# 例によって、答え丸写し（C++しかなかったから、自分なりに書き直した）
# TODO edit this code

# param
'''N = int(input())
list = []
for i in range(N):
    a, b = map(str, input().split())
    list.append(a)
    list.append(b)




# solve
ans = 0

# answer
print(ans)'''
