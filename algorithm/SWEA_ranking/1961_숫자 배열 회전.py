import sys
import copy
sys.stdin = open("1961_숫자 배열 회전.txt", "r")
testcase = int(sys.stdin.readline())
# testcase = int(input())

for t in range(1, testcase + 1):
    print(f'#{t}', end='\n')
    N = int(sys.stdin.readline())
    # N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, sys.stdin.readline().split())))
        # arr.append(list(map(int, input().split())))

    new_arr = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(len(new_arr[0])):
        for j in range(len(new_arr)):
            new_arr[i][j] = arr[j][i]
    
    new_arr1 = copy.deepcopy(new_arr)
    arr_1 = []
    for i in range(len(arr)):
        new_arr1[i].reverse()
        arr_1.append(new_arr1[i])
    
    new_arr2 = arr[:]
    arr_2 = []
    for i in reversed(range(len(arr))):
        new_arr2[i].reverse()
        arr_2.append(new_arr2[i])

    new_arr3 = new_arr
    arr_3 = []
    for i in reversed(range(len(arr))):
        new_arr3[i]
        arr_3.append(new_arr3[i])

    for r in range(len(arr_1)):
        for arr in [arr_1, arr_2, arr_3]:
            for num in arr[r]:
                print(num, end='')
            print(end=' ')
        print()