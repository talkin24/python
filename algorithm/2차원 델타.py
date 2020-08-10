arr = [[0,1,2,3],
       [4,5,6,7],
       [8,9,10,11]
       ]

n = len(arr)
m = len(arr[0])

visited = [[0 for _ in range(m)] for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for x in range(len(arr)):
    for y in range(len(arr[0])):
        for i in range(4):
            testX = x + dx[i]
            testY = y + dy[i]
            if 0 <= testX < n and 0 <= testY < m and visited[testX][testY] == 0:
                print(arr[testX][testY], end=' ')
                visited[testX][testY] = 1