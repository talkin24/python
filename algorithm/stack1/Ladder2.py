import sys
import copy

sys.stdin = open("Ladder2.txt.", "r")

for t in range(1, 11):
    print(f"#{int(input())}", end=" ")
    arr = [list(map(int, input().split())) for _ in range(100)]
    for row in arr:
        row.insert(0, 0)
        row.append(0)
    results = {}
    for i in range(1, len(arr[0]) - 1):
        temp = copy.deepcopy(arr)
        if temp[0][i] == 1:
            now_r = 0
            now_c = i
            temp[now_r][now_c] = 3
            results[i] = 0
            while now_r != 99:
                if (temp[now_r + 1][now_c] == 1) & (temp[now_r][now_c + 1] in [0, 3]) & (temp[now_r][now_c - 1] in [0, 3]):
                    now_r += 1
                else:
                    if (temp[now_r][now_c + 1] == 1) & (temp[now_r][now_c - 1] in [0, 3]):
                        now_c += 1
                    elif (temp[now_r][now_c + 1] in [0, 3]) & (temp[now_r][now_c - 1] == 1):
                        now_c -= 1
                temp[now_r][now_c] = 3
                results[i] += 1
    min_value = results[1]
    for k, v in results.items():
        if min_value >= v:
            min_value = v
            min_key = k
    print(min_key - 1)

