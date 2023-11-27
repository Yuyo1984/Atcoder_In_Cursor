# TODO edit this code

# param
x = int(input())

# solve
ans = 0
if x >= 0 and x < 40:
    ans = 40 - x
elif x >= 40 and x < 70:
    ans = 70 - x
elif x >= 70 and x < 90:
    ans = 90 - x
else:
    ans = "expert"


# answer
print(ans)
