import sys

sys.stdin = open("Ladder1.txt.", "r")

for t in range(1, 11):
    print(f"#{int(input())}", end=" ")
    arr = [list(map(int, input().split())) for _ in range(100)]
    for row in arr:
        row.insert(0, 0)
        row.append(0)
    for i in range(1, len(arr[99]) - 1):
        if arr[99][i] == 2:
            now_r = 99
            now_c = i
            arr[now_r][now_c] = 3
            while now_r != 0:
                if (arr[now_r - 1][now_c] == 1) & (arr[now_r][now_c + 1] in [0, 3]) & (arr[now_r][now_c - 1] in [0, 3]):
                    now_r -= 1
                else:
                    if (arr[now_r][now_c + 1] == 1) & (arr[now_r][now_c - 1] in [0, 3]):
                        now_c += 1
                    elif (arr[now_r][now_c + 1] in [0, 3]) & (arr[now_r][now_c - 1] == 1):
                        now_c -= 1
                arr[now_r][now_c] = 3
    print(now_c - 1)

