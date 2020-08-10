import sys
sys.stdin = open("sum.txt", "r")


testcase = 10
for t in range(1,testcase+1):
    print(f'#{t}', end=' ')
    n = int(sys.stdin.readline())
    array = []
    for _ in range(100):
        array.append(list(map(int, sys.stdin.readline().split())))

# for t in range(1,testcase+1):
#     print(f'#{t}', end=' ')
#     n = int(input())
#     array = []
#     for _ in range(100):
#         array.append(list(map(int, input().split())))
    max_sum = 0

    for x in range(len(array)):
        row_sum = 0
        for y in range(len(array[0])):
            row_sum += array[x][y]
        if max_sum < row_sum:
            max_sum = row_sum

    for y in range(len(array[0])):
        col_sum = 0
        for x in range(len(array)):
            col_sum += array[x][y]
        if max_sum < col_sum:
            max_sum = col_sum

    dia1_sum = 0
    for x in range(len(array)):
        dia1_sum += array[x][x]
    if max_sum < dia1_sum:
        max_sum = dia1_sum

    dia2_sum = 0
    for x in range(len(array)):
        dia2_sum += array[99-x][x]
    if max_sum < dia2_sum:
        max_sum = dia2_sum

    print(max_sum)

