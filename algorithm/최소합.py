'''
3
3
1 2 3
2 3 4
3 4 5
4
2 4 1 3
1 1 7 1
9 1 7 10
5 7 2 4
5
6 7 1 10 2
10 2 7 5 9
9 3 2 9 6
1 6 8 2 9
8 3 8 2 1
'''

def find(arr, i, j, num):
    global result
    if i == N - 1 and j == N - 1:
        num += arr[i][j]

        if num < result:
            result = num
    else:
        num += arr[i][j]
        if i != N - 1:
            find(arr, i + 1, j, num)
        if j != N - 1:
            find(arr, i, j + 1, num)


T = int(input())
for t in range(1, T + 1):
    print(f'#{t}', end=' ')

    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = float('inf')
    find(arr, 0, 0, 0)
    print(result)




