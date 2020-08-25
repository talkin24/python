import sys

sys.stdin = open("문자열 비교.txt", "r")
testcase = int(sys.stdin.readline())
# testcase = int(input())

for t in range(1, testcase + 1):
    print(f'#{t}', end=' ')

    p, t = sys.stdin.readline(), sys.stdin.readline()
    # p, t = input(), input()

    check = 0
    i, j = 0, 0
    while i < len(t) and j < len(p):
        if t[i] != p[j]:
            i = i - j
            j = -1
        i += 1
        j += 1
        if j == len(p) - 1: check = 1

    print(check)
