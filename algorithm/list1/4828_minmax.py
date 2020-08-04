import sys
sys.stdin = open("4828_minmax.txt", "r")

testcase = int(sys.stdin.readline())

for t in range(1,testcase+1):
    print(f'#{t}', end=' ')
    n = int(sys.stdin.readline())
    L = list(map(int, sys.stdin.readline().split()))

# testcase = int(input())

# for t in range(1,testcase+1):
#     print(f'#{t}', end=' ')
#     n = int(input())
#     L = list(map(int, input().split()))
    max, min = L[0], L[0]
    for i in range(len(L)):
        if L[i] > max:
            max = L[i]
    for i in range(len(L)):
        if L[i] < min:
            min = L[i]
    result = max - min
    print(result)