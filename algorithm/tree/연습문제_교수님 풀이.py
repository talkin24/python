'''
13
1, 2, 1, 3, 2, 4, 3, 5, 3, 6, 4, 7, 5, 8, 5, 9, 6, 10, 6, 11, 7, 12, 11, 13
'''
def preorder(node):
    if node != 0:
        print(node, end = " ")
        preorder(tree[node][0])
        preorder(tree[node][1])
def postorder(node):
    if node != 0:
        postorder(tree[node][0])
        postorder(tree[node][1])
        print(node, end = " ")


V = int(input()) # 정점
E = V - 1 # 간선
tree = [[0] * 3 for _ in range(V + 1)]
temp = list(map(int, input().split(',')))
# tree 저장
for i in range(E):
    p, c = temp [i * 2], temp[i * 2 + 1]
    if tree[p][0] == 0:
        tree[p][0] = c # left
    else:
        tree[p][1] = c # right
    tree[c][2] = p # parent

print(tree)
# for t in tree:
#     print(*t)

preorder(1)
print()
postorder(1)