# TODO edit this code

# param
s1 = input().rstrip('\r')
s2 = input().rstrip('\r')
s3 = input().rstrip('\r')
t = input()
# solve
ans = []
for i in range(len(t)):
    if t[i] == "1":
        ans.append(s1)
    elif t[i] == "2":
        ans.append(s2)
    else:
        ans.append(s3)

# answer
print("".join(ans))
