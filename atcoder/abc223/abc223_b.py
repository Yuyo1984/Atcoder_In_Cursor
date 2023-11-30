# 分からなかったので答え丸写し
# やってることは文字列のk番目から最後と最初からk-1番目までをくっつけていって、リストを作って比較。
# 文字列のずらし方ってこうやるんだな・・・
s = input()
n = len(s)
v = []
for k in range(0, n):
    v.append(s[k:n] + s[0:k])
print(min(v))
print(max(v))
