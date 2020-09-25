# bfs로 체크
def bomb(r, c): # 좌표 입력
    global result
    Q = [] # 빈 큐
    visit = [[0] * N for _ in range(N)] # 방문 확인
    Q.append([r, c])
    visit[r][c] = 1
    while Q:
        v = Q.pop(0)
        b = arr[v[0]][v[1]] # 폭발 범위
        if b != 0:  # 폭탄이 존재할 때
            result += 1 # 폭탄 개수 체크
            visit[v[0]][v[1]] = 1   # 방문 체크
            r1 = v[0] # 새 좌표
            c1 = v[1]
            for dr in range(-b, b + 1):
                if 0 <= (r1 + dr) <= (N - 1) and visit[r1 + dr][c1] == 0: # 상하 체크, 범위 안에 존재하고, 방문하지 않았을때
                    if [r1 + dr, c1] not in Q: # 중복 방지
                        Q.append([r1 + dr, c1])
            for dc in range(-b, b + 1):
                if 0 <= (c1 + dc) <= (N - 1) and visit[r1][c1 + dc] == 0: # 좌우 체크, 범위 안에 존재하고, 방문하지 않았을때
                    # print(r, c + dc)
                    if [r1, c1 + dc] not in Q:
                        Q.append([r1, c1 + dc])



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
