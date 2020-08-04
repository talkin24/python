import sys
sys.stdin = open("Flatten.txt", "r")

testcase = 10

for t in range(1,testcase+1):
    print(f'#{t}', end=' ')
    n = int(sys.stdin.readline())
    L = list(map(int, sys.stdin.readline().split()))

for t in range(1, 11):
    print(f'#{t}', end=' ')
    n = int(input())
    L = list(map(int, input().split()))

    for i in range(n):
        L = sorted(L)
        L[0] = L[0] + 1
        L[-1] = L[-1] - 1

    L = sorted(L)
    print(L[-1] - L[1])
