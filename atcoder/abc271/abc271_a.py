print("{:02X}".format(int(input())))
# ラストだけWA出してしまったので、多分何かミスってる
# 解説のコードが簡潔すぎる・・・覚えておこう
# TODO edit this code

'''
# param
N = int(input())


def hex(N):
    ans = ''
    while N % 16 != 0:
        if N % 16 >= 16:
            return -1
        x = ''
        if N % 16 == 10:
            x = 'A'
        elif N % 16 == 11:
            x = 'B'
        elif N % 16 == 12:
            x = 'C'
        elif N % 16 == 13:
            x = 'D'
        elif N % 16 == 14:
            x = 'E'
        elif N % 16 == 15:
            x = 'F'
        else:
            x = str(N % 16)
        ans += x
        N //= 16

    if len(ans) == 1:
        ans += '0'
    elif len(ans) == 0:
        ans += "00"
    return ans[::-1]


print(hex(N))
'''
