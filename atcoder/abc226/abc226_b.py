# 全く思いつかなかった・・・多分例2の考えをうまく落とし込めればいける。
# 全探索は恐らくTLE
# 新しく出てきた要素に着目する・・・？
# TODO edit this code

# 以下、解説の写し

'''
解説見て、自分で書いてみたけど、ダメだったやつ
# param
n = int(input())
s = set()

# solve
ans = 0
for i in range(n):
    a = list(map(int, input().split()))
    L = a.pop(0)
    for j in range(L):
        s.add(a[j])

# answer
print(len(s))
'''

N = int(input())
print(len(set(input()for i in range(N))))
