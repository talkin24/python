import sys
sys.stdin = open("1976_시각 덧셈.txt", "r")
testcase = int(sys.stdin.readline())
# testcase = int(input())

for t in range(1, testcase + 1):
    print(f'#{t}', end=' ')

    arr = list(map(int, sys.stdin.readline().split()))
    # arr = list(map(int, input().split()))

    h = arr[0] + arr[2]
    m = arr[1] + arr[3]

    if m > 60:
        h = h + 1
        m = m - 60
    if h > 12:
        h = h - 12
    print(h, m)