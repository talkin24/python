import sys
sys.stdin = open('노드의 합.txt', 'r')
T = int(input())
for t in range(1, T + 1):
    print(f'#{t}', end=" ")
    N, M, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(M)]
    print(N, M, L, arr)
