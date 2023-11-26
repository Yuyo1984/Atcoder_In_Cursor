# 30分でギブアップ、正解は前日比を記録する形で累積和を使う。

# 入力
D = int(input())
N = int(input())
LR = []
for i in range(N):
    LR.append(list(map(int, input().split())))

# 来日者数の前日比を記録するリストを作成。
ans = []
for j in range(D+2):
    ans.append(0)

# 前日比を出す
for k in LR:
    x = k[0]
    y = k[1] + 1
    ans[x] += 1
    ans[y] -= 1

# 解答を出力。出したいのは来日者数なので、数列のように前日迄の来日者数を一時保存する変数を作って、足し合わせていく。
tmp = ans[1]
for m in range(1, D+1):
    print(tmp)
    tmp += ans[m+1]
