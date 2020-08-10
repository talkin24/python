import sys
sys.stdin = open("스도쿠 검증.txt", "r")

testcase = int(sys.stdin.readline())
# testcase = int(input())
def check_sdoku(arr):
    for m in range(len(arr)):
        dic = {}
        for number in arr[m]:
            dic[number] = arr[m].count(number)
        if 2 in dic.values():
            return 0

    for n in range(len(arr[0])):
        arr_c = []
        for m in range(len(arr)):
            arr_c.append(arr[m][n])
        dic = {}
        for number in arr_c:
            dic[number] = arr_c.count(number)
        if 2 in dic.values():
            return 0

    for i in range(0, len(arr), 3):
        for j in range(0, len(arr[0]), 3):
            arr_33 = []
            for di in range(3):
                for dj in range(3):
                    arr_33.append(arr[i + di][j + dj])
            dic = {}
            for number in arr_33:
                dic[number] = arr_33.count(number)
            if 2 in dic.values():
                return 0
    return 1
for t in range(1,testcase+1):
    print(f'#{t}', end=' ')
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
    # arr = [list(map(int, input().split())) for _ in range(9)]

    print(check_sdoku(arr))






