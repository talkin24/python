import sys
sys.stdin = open("4836_색칠하기.txt", "r")

testcase = int(sys.stdin.readline())
# testcase = int(input())
for t in range(1,testcase+1):
    print(f'#{t}', end=' ')
    n = int(sys.stdin.readline())
    # n = int(input())

    dir = []
    for _ in range(n):
        dir.append(list(map(int, sys.stdin.readline().split())))
        # dir.append(list(map(int, input().split())))
    arr = []
    for _ in range(10):
        row = []
        for _ in range(10):
            row.append(0)
        arr.append(row)

    for i in range(len(dir)):
        r1, c1, r2, c2, color = dir[i]

        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                arr[r][c] += color

    pupple = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 3:
                pupple += 1
    print(pupple)


