V = 13
arr = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6, 4, 7, 5, 8, 5, 9, 6, 10, 6, 11, 7, 12, 11, 13]

right = [0] * 14
left = [0] * 14
father = [0] * 14
visited = [0] * 14

for i in range(0, 24, 2):
    F = arr[i]
    S = arr[i + 1]
    if left[F] == 0:
        left[F] = S
    elif left[F] != 0:
        right[F] = S
    father[S] = F

print(left)
print(right)
print(father)

root = 1
s = []

while len(s) != 13:
    if visited[root] == 0:
        s.append(root) # 스택에 루트 추가
    visited[root] = 1 # 방문 표시

    l = left[root]
    r = right[root]
    if l != 0 and visited[l] == 0:
        root = l
    elif visited[l] != 0 and r != 0 and visited[r] == 0:
        root = r
    elif (l == 0 or visited[l] != 0) and (r == 0 or visited[r] != 0):
        root = father[root]
print(s)

