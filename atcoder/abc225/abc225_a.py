S = input()

ans = 0
counter = 0

for i in range(-1, 2):
    if S[i] == S[i+1]:
        counter += 1

div = 1
if counter == 1:
    div = 2
if counter == 3:
    div = 6
ans = 6 // div

print(ans)
