# TODO edit this code

# param
s, t = map(int, input().split())
# solve
ans = 0
for a in range(s+1):
    for b in range(s+1-a):
        for c in range(s+1-a-b):
            if a * b * c <= t:
                ans += 1

# answer
print(ans)
