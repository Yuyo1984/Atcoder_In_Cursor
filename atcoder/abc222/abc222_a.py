# TODO edit this code

# param
N = input()

# solve
ans = ''
x = len(N)
if x <= 4:
    for n in range(4 - x):
        ans += '0'
ans += N

# answer
print(ans)
