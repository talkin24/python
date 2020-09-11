import sys
sys.stdin = open('이진탐색.txt', 'r')
T = int(input())

def inorder(node): # 중위 순회
    global cnt
    if node != 0:
        inorder(tree[node][0])
        cnt += 1 # 현재 노드 카운트 증가(순서 저장)
        tree[node][2] = cnt # 카운트 현재 노드에 저장
        inorder(tree[node][1])


    tree = [[0] * 3 for _ in range(N + 1)]

    for i in range(1, int(N / 2) + 1): # 이진트리 생성
        if 2 * i < N + 1: # 인덱스 제한
            tree[i][0] = 2 * i # Left child
        if 2 * i + 1 < N + 1: # 인덱스 제한
            tree[i][1] = 2 * i + 1 # Right child
    cnt = 0 # 카운트 초기화
    inorder(1)
    print(tree[1][2], tree[N//2][2]) # 루트(1), N/2번 노드(N//2)
