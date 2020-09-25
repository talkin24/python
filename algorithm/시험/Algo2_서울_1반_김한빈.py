'''
3
10 8 17
0 0
1 0
1 1
4 2
4 3
4 5
2 4
3 4
7 4
8 4
9 4
7 5
8 5
9 5
7 6
8 6
9 6
10 10 3
5 5
4 4
6 6
5 3 6
0 2
1 2
2 2
3 2
4 2
4 0

'''

T = int(input())
for t in range(1, T + 1):
    print(f"#{t}", end=" ")
    # M(마당 가로 길이), N(마당 세로 길이), K(연못 좌표 개수) 입력
    M, N, K = map(int, input().split())
    # 빈 arr 생성 + 각 상하좌우로 1씩 padding을 준다
    arr = [[0] * (M + 2) for _ in range(N + 2)]
    # 연못의 좌표 입력, 단 padding 감안하여 1씩 더한 것에 유의할 것
    for _ in range(K):
        X, Y = map(int, input().split())
        arr[Y + 1][X + 1] = 1
    # 상하좌우
    # D = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    D = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    # 좌표 하나씩 확인
    i = 2
    for r in range(len(arr)):
        for c in range(len(arr[0])):
            # 1 즉 연못이면 i 값을 부여
            if arr[r][c] == 1:
                arr[r][c] = i
                # 해당 좌표의 상하좌우가 만약 연못이라면 같은 i 값을 부여
                for d in D:
                    if arr[r + d[0]][c + d[1]] == 1:
                        arr[r + d[0]][c + d[1]] = i

        # 다른 연못 구별을 위해 row 증가 시 마다 i 증가
        i += 1

    print(arr)
    pond = []
    # 전체 i 값 모아서 set함수를 통해 연못 개수 구하기
    for r in range(len(arr)):
        for c in range(len(arr[0])):
            if arr[r][c] != 0:
                pond.append(arr[r][c])
    # set의 길이가 연못의 개수
    print(len(set(pond)))


