# TODO edit this code

# param
a, b = map(int, input().split())

# solve
for i in range(0, 256):
    if a ^ i == b:
        print(i)
