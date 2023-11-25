N = int(input())
B = []

while len(B) < 10:
    if N % 2 == 0:
        B.insert(0, 0)
    else:
        B.insert(0, 1)
    N //= 2

ans = ''

for i in B:
    ans += str(i)
    
print(ans)