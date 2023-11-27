# TODO edit this code

# param
n = int(input())

# solve
ans = 0
k = 0
while 2 ** k <= n:
    k += 1
    ans = k-1
# answer
print(ans)
