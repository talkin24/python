import sys
sys.stdin = open("행렬찾기.txt", "r")

# testcase = int(sys.stdin.readline())
testcase = int(input())
def matrix_check(arr, r, c):
        r_len, c_len = 0, 0
        matrix = []
        for dr in range(len(arr) - r):
            if arr[r + dr][c] != 0:
                r_len += 1
            else:
                matrix.append(r_len)
                break
        for dc in range(len(arr[r]) - c):
            if arr[r][c + dc] != 0:
                c_len += 1
            else:
                matrix.append(c_len)
                break
        matrix.append(r_len*c_len)
        matrixs.append(matrix)

for t in range(1,testcase+1):
    print(f'#{t}', end=' ')
    # n = int(sys.stdin.readline())
    n = int(input())
    # arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    arr = [list(map(int, input().split())) for _ in range(n)]

    matrixs = []
    for r in range(len(arr)):
        for c in range(len(arr[r])):
            if r > 0 and c > 0:
                if arr[r - 1][c] == 0 and arr[r][c - 1] == 0:
                    matrix_check(arr, r, c)
            elif r == 0 and c == 0:
               matrix_check(arr, r, c)
            elif r == 0 and c > 0:
                if arr[r][c-1] == 0:
                    matrix_check(arr, r, c)
            elif r > 0 and c == 0:
                if arr[r-1][c] == 0:
                    matrix_check(arr, r, c)

    matrixs = [matrix for matrix in matrixs if matrix != [0, 0, 0]]
    print(len(matrixs), end=' ')

    while matrixs != []:
        min = matrixs[0]
        for matrix in matrixs:
            if matrix[2] < min[2]:
                min = matrix
            elif matrix[2] == min[2]:
                if matrix[0] < min[0]:
                    min = matrix
        print(min[0], min[1], end=' ')
        matrixs.remove(min)
    print()






