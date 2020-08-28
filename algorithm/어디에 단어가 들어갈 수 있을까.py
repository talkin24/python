import sys

sys.stdin = open("어디에 단어가 들어갈 수 있을까.txt", "r")
T = int(input())
for t in range(1, T + 1):
    print(f"#{t}", end=" ")
    N, K = input().split()
    N, K = int(N), int(K)
    arr = [list(map(int, input().split())) for _ in range(N)]

    results = []
    for row in arr:
        line = 0
        for i in range(len(row)):
            if row[i] == 1:
                if i == len(row) - 1:
                    line += 1
                    results.append(line)
                else:
                    line += 1
            elif row[i] == 0:
                results.append(line)
                line = 0

    for c in range(len(arr[0])):
        col = []
        for r in range(len(arr)):
            col.append(arr[r][c])
            line = 0
        for i in range(len(col)):
            if col[i] == 1:
                if i == len(col) - 1:
                    line += 1
                    results.append(line)
                else:
                    line += 1
            elif col[i] == 0:
                results.append(line)
                line = 0

    print(results.count(K))