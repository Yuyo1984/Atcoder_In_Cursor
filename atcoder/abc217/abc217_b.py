# TODO edit this code

# param
contest = ["ABC", "ARC", "AGC", "AHC"]
Flag = [True for i in range(4)]

for j in range(3):
    str = input().rstrip('\r')
    for k in range(4):
        if (str == contest[k]):
            Flag[k] = False

for m in range(4):
    if Flag[m]:
        print(contest[m])
