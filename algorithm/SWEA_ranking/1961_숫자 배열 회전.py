import sys
sys.stdin = open("1961_숫자 배열 회전.txt", "r")
testcase = int(sys.stdin.readline())
# testcase = int(input())

for t in range(1, testcase + 1):
    print(f'#{t}', end='\n')
    N = int(sys.stdin.readline())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, sys.stdin.readline().split())))

    new_arr = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(len(new_arr[0])):
        for j in range(len(new_arr)):
            new_arr[i][j] = arr[j][i]
    
    new_arr1 = new_arr[:]
    arr_1 = []
    new_arr1[0].reverse()
    arr_1.append(new_arr1[0])
    new_arr1[1].reverse()
    arr_1.append(new_arr1[1])
    new_arr1[2].reverse()
    arr_1.append(new_arr1[2])
    print(arr_1)

    arr_3 = []
    arr_3.append(new_arr[2])
    arr_3.append(new_arr[1])
    arr_3.append(new_arr[0])
    print(arr_3)

