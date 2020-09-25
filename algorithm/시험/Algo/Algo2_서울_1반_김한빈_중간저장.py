def bomb(r, c):
    global result
    Q = []
    visit = [[0] * N for _ in range(N)]
    # if arr[r][c] != 0:
    Q.append([r, c])
    visit[r][c] = 1
    while Q:
        v = Q.pop(0)
        b = arr[v[0]][v[1]]
        if b != 0:
            result += 1
            print(v[0], v[1])
            visit[v[0]][v[1]] = 1

            for dr in range(-b, b + 1):
                if 0 <= (r + dr) <= (N - 1) and visit[r + dr][c] == 0:
                    # print(r + dr, c)
                    Q.append([r + dr, c])
                    # visit[r + dr][c] = 1
            for dc in range(-b, b + 1):
                # print(dc)
                if 0 <= (c + dc) <= (N - 1) and visit[r][c + dc] == 0:
                    # print(r, c + dc)
                    Q.append([r, c + dc])
                    # visit[r][c + dc] = 1


T = int(input())    # 테스트 케이스 입력
for t in range(1, T + 1):
    print(f'#{t}', end=" ")
    N = int(input()) # 지도의 크기 입력
    R, C = map(int, input().split())     # 첫 폭탄 입력
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    bomb(R, C)
    print(result)

'''
3                
4
3 3
0 0 1 0
0 2 0 1
0 0 0 0
1 1 0 2
6
3 2
0 0 0 0 0 0
0 0 3 0 1 1
1 0 0 0 0 0
0 0 3 0 0 2
2 0 0 0 0 0
0 1 0 2 0 2
10
8 7
0 3 0 0 3 0 0 0 0 0
0 3 0 0 0 0 0 1 0 3
0 0 5 0 0 0 0 0 3 0
0 0 0 0 0 0 0 0 0 0
0 5 0 0 0 2 0 5 0 0
0 0 0 0 0 3 0 2 0 4
4 0 2 0 0 2 1 4 0 0
0 0 0 0 0 5 0 0 0 0
0 0 0 0 0 0 4 5 5 1
3 0 3 0 2 4 0 0 0 1
'''

    # # print(r, c)
    # if arr[r][c] != 0:
    #     result += 1
    #     b = arr[r][c]
    #
    #     for b in range(1, b + 1):
    #         if 0 <= (r - b) <= (N-1):
    #             bomb(r - b, c)
    #         if 0 <= (r + b) <= (N-1):
    #             bomb(r + b, c)
    #         if 0 <= (c - b) <= (N-1):
    #             bomb(r, c - b)
    #         if 0 <= (c + b) <= (N-1):
    #             bomb(r, c + b)