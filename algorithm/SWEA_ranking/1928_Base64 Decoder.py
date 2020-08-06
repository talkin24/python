import sys
sys.stdin = open("1928_Base64 Decoder.txt", "r")
testcase = int(sys.stdin.readline())
# testcase = int(input())
chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
dic = {}
for v, c in enumerate(chars):
    dic[c] = v

for t in range(1, testcase + 1):
    print(f'#{t}', end=' ')
    code = sys.stdin.readline().split()[0]
    # code = input()

    for n in range(0, len(code), 4):
        buffer = ''
        for c in code[n:n + 4]:
            num10 = dic[c]
            num2 = format(num10, 'b')
            num2 = '0' * (6 - len(num2)) + num2
            buffer += num2

        L = [int(buffer[0:8], 2), int(buffer[8:16], 2), int(buffer[16:24], 2)]
        for a in L:
            print(chr(a), end='')
    print()