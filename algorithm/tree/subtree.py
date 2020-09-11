import sys

def inorder(node): # 순회 종류는 상관 없이 서브트리 개수만 알아내면 되므로 어떤 순회 방법을 써도 괜찮다. 여기선 중위 순회 사용
    global nodes
    if node != 0:
        inorder(tree[node][0]) # left child
        nodes.append(node) # parent (nodes에 저장)
        inorder(tree[node][1]) # right child

sys.stdin = open('subtree.txt', 'r')
T = int(input())

for t in range(1, T + 1):
    print(f'#{t}', end=" ")
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))

    V = E + 1 # 정점의 개수
    tree = [[0] * 2 for _ in range(V + 1)] # 빈 트리 생성[left child, right child]
    for i in range(E):
        p, c = arr[i * 2], arr[i * 2 + 1] # 부모, 자식
        if tree[p][0] == 0: # left child의 자리가 비어있으면
            tree[p][0] = c  # left
        else:
            tree[p][1] = c  # right

    nodes = []
    inorder(N)
    print(len(nodes)) # nodes 길이 프린트

