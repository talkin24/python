# dfs with recurrence

'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

def dfs(v):
    # 방문체크
    visited[v] = 1
    print(v, end=" ")
    # v의 인접한 정점 중에서 방문 안한 정점을 재귀 호출
    for w in range(1, N+1):
        if G[v][w] == 1 and visited[w] == 0:
            dfs(w)

def dfs2(v):
    s = []
    s.append(v)
    while len(s) != 0:
        v = s.pop()
        if not visited[v]:
            visited[v] = 1
            print(v, end=" ")
            for w in range(1, v+1):
                if G[v][w] == 1 and visited[w] == 0:
                    s.append(w)


# 정점, 간선
N, E = map(int, input().split())
# 간선들...
temp = list(map(int, input().split()))
# 인접행렬
G = [[0] * (N+1) for _ in range(N+1)]
visited = [0] * (N + 1)
# 간선들을 인접행렬에 저장
for i in range(E):
    s, e = temp[2*i], temp[2*i+1]
    G[s][e] = 1
    G[e][s] = 1

dfs(1)
dfs2(1)