

#下のコードは自分が書いたもの
#ご覧の通り愚直にやっているが計算量が膨れ上がるのでTLE出されるのは必至

''' import math

n, m = int(input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

min_abs = 10 ** 9

for i in range(n):
    for j in range(m):
        x = abs(i - j)
        if(x <= min_abs):
            min_abs = x
            
print(min_abs) '''