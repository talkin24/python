import sys

def hm(str):
    check = True
    for i in range(len(str) // 2):
        if str[i] != str[-1 - i]:
            check = False
            break
    return check
 
sys.stdin = open("회문2.txt", "r")

for t in range(1, 11):
    # print(f'#{sys.stdin.readline()[:-1]}', end=' ')
    print(f'#{input()}', end=' ')

    # arr = [sys.stdin.readline()[:-1] for _ in range(100)]
    arr = [input() for _ in range(100)]

    pal = 1
    for row in arr:
        for i in range(3, len(row) + 1):
            for j in range(len(row) - i + 1):
                if hm(row[j:j + i]) and i > pal:
                    pal = i
                    # print(row[j:j + i])
    for c in range(len(arr[0])):
        col = ""
        for r in range(len(arr)):
            col += arr[r][c]
        for i in range(3, len(col) + 1):
            for j in range(len(col) - i + 1):
                if hm(col[j:j + i]) and i > pal:
                    pal = i
                    # print(col[j:j + i])
    print(pal)