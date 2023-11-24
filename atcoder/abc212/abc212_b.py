# 解けなかったので解説を写経
# それぞれ判別方法を分けて、真偽を判別するべきだった
# フラグを立てて判別する方法は間違ってなかった

a = input()
same, step = True, True

for i in range(3):
    if a[i] != a[i+1]:
        same = False
    if (int(a[i]) + 1) % 10 != int(a[i+1]):
        step = False
        
if (same or step):
    print("Weak")
else:
    print("Strong")