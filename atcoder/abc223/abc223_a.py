# TODO edit this code

# param
N = int(input())

# solve
flag = False
if N % 100 == 0 and N != 0:
    flag = True
# answer
if flag:
    print('Yes')
else:
    print('No')
