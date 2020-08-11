import sys
sys.stdin = open("1959_두 개의 숫자열.txt", "r")
testcase = int(sys.stdin.readline())
# testcase = int(input())

for t in range(1, testcase + 1):
    print(f'#{t}', end=' ')
    L = list(map(int, sys.stdin.readline().split()))
    # L = list(map(int, input().split()))
    N, M = L[0], L[1]
    A = list(map(int, sys.stdin.readline().split()))
    # A = list(map(int, input().split()))
    B = list(map(int, sys.stdin.readline().split()))
    # B = list(map(int, input().split()))
    
    muls = []
    if N >= M:
        L, S = N, M
        L_line, S_line = A, B
    else:
        L, S = M, N
        L_line, S_line = B, A
    for i in range(L - S + 1):
        mul = 0
        for j in range(S):
            mul += L_line[i + j] * S_line[j]
        muls.append(mul)
    
    max_mul = muls[0]
    for mul in muls:
        if mul > max_mul:
            max_mul = mul
    print(max_mul)