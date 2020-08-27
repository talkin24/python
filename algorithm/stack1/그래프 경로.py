import sys

def dfs(v):
    s = []
    s.append(v)
    while len(s) != 0:
        v = s.pop()
        if not visited[v]:
            visited[v] = 1
            for w in range(1, V + 1):
                if adj[v][w] == 1 and visited[w] == 0:
                    s.append(w)

sys.stdin = open("그래프 경로.txt", "r")
tests = int(input())
for t in range(1, tests + 1):
    print(f"#{t}", end=" ")
    V, E = map(int, input().split())
    adj = [[0] * (V + 1) for _ in range(V + 1)]
    for _ in range(E):
        r, c = map(int, input().split())
        adj[r][c] = 1
    S, G = map(int, input().split())

    visited = [0] * (V + 1)

    dfs(S)
    if visited[G]:
        print(1)
    else:
        print(0)


