import sys
sys.stdin = open("달팽이 숫자.txt", "r")

testcase = int(sys.stdin.readline())
# testcase = int(input())
for t in range(1,testcase+1):
    print(f'#{t}', end='\n')
    n = int(sys.stdin.readline())
    # n = int(input())
    arr = [[0 for _ in range(n)] for _ in range(n)]

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    x, y, newX, newY, i = 0, 0, 0, 0, 0

    for num in range(1, n ** 2 + 1):
        x, y = newX, newY
        arr[x][y] = num
        newX = x + dx[i]
        newY = y + dy[i]
        if newX >= n or newX < 0 or newY >= n or newY < 0 or arr[newX][newY] != 0:
            i = (i + 1) % 4
            newX = x + dx[i]
            newY = y + dy[i]

    for i in range(n):
        for j in range(n):
            print(arr[i][j], end=' ')
        print()

