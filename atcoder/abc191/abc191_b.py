# TODO edit this code

# param
N, X = map(int, input().split())
A = [*map(int, input().split())]

# solve
ans = []
for i in A:
    if i != X:
        ans.append(i)

# answer
for j in ans:
    print(j, end=' ')
