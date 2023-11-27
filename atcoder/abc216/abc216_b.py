# TODO edit this code

# param
n = int(input())
name = []
for i in range(n):
    name.append(list(input().split()))
# solve
ans = 'No'
for j in range(n):
    for k in range(j+1, n):
        if (name[j][0] == name[k][0]) and (name[j][1] == name[k][1]):
            ans = 'Yes'

# answer
print(ans)
