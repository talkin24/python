arr = [[1,2,3],
       [4,5,6],
       [7,8,9]
       ]
N = len(arr)
M = len(arr[0])

# 행우선
for i in range(N):
    for j in range(M):
        print(arr[i][j], end=" ")
    print()
print()


# 열우선
for j in range(M):
    for i in range(N):
        print(arr[i][j], end=" ")
    print()
print()
