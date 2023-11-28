# TODO edit this code

# param
s = list(input().rstrip('\r'))
t = input()
# solve
sort_s = []
n = len(s) - 1
for i in range(n+1):
    if i == 0:
        sort_s.append(s)
    else:
        j = s.copy()
        j[i-1], j[i] = j[i], j[i-1]
        sort_s.append(j)

# answer
flag = False
for i in range(len(sort_s)):
    x = sort_s[i]
    x = "".join(x)
    if x == t:
        flag = True
        break

if flag:
    print('Yes')
else:
    print('No')
