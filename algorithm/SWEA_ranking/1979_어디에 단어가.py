import sys

sys.stdin = open("1979_어디에 단어가.txt", "r")
# for n in range(1, int(sys.stdin.readline()) + 1):
for n in range(1, int(input()) + 1):
    print(f"#{n}", end=' ')

    # arr = list(map(int, sys.stdin.readline().split()))
    arr = list(map(int, input().split()))
    N = arr[0]
    K = arr[1]
    # puzzle = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    puzzle = [list(map(int, input().split())) for _ in range(N)]

    whites_row = []
    for row in puzzle:
        cnt = 0
        for i in range(N):
            if row[i] == 1:
                cnt += 1
                if i == N-1:
                    whites_row.append(cnt)
                    cnt = 0
            else:
                whites_row.append(cnt)
                cnt = 0
    result1 = whites_row.count(K)

    whites_col = []
    for c in range(N):
        col = []
        for r in range(N):
            col.append(puzzle[r][c])
        cnt = 0
        for i in range(N):
            if col[i] == 1:
                cnt += 1
                if i == N-1:
                    whites_col.append(cnt)
                    cnt = 0
            else:
                whites_col.append(cnt)
                cnt = 0
    result2 = whites_col.count(K)

    print(result1 + result2)




