import sys

def hm(str):
    check = 1
    for i in range(len(str)//2 - 1):
        if str[i] != str[-1-i]:
            check = 0
    return check

sys.stdin = open("회문.txt.", "r")
testcase = int(sys.stdin.readline())
# testcase = int(input())
for t in range(1, testcase + 1):
    print(f'#{t}', end=" ")

    N, M = map(int, sys.stdin.readline().split())
    # N, M = map(int, input().split())
    arr = [sys.stdin.readline()[:-1] for _ in range(N)]
    # arr = [input() for _ in range(N)]

    for row in arr:
        for i in range(N - M + 1):
            if hm(row[i:i+M]) == 1:
                print(row[i:i+M])

    for j in range(len(arr[0])):
        col = ""
        for i in range(len(arr)):
           col += arr[i][j]
        for i in range(N - M + 1):
            if hm(col[i:i+M]) == 1:
                print(col[i:i+M])
