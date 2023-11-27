# TODO edit this code

# param
num_list = [*map(int, input().split())]
alpha_raw = "abcdefghijklmnopqrstuvwxyz"

ans = []
for i in num_list:
    for j in alpha_raw:
        if alpha_raw[i-1] == j:
            ans.append(j)

print("".join(ans))
