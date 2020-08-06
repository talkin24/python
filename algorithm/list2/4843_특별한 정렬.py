import sys
sys.stdin = open("4843_특별한 정렬.txt", "r")

testcase = int(sys.stdin.readline())
# testcase = int(input())
for t in range(1,testcase+1):
    print(f'#{t}', end=' ')
    n  = int(sys.stdin.readline())
    L = list(map(int, sys.stdin.readline().split()))
    # n = int(input())
    # L = list(map(int, input().split()))

    result = []
    while L != []:
        min_ = L[0]
        max_ = L[0]
        for i in range(len(L)):
            if L[i] > max_:
                max_ = L[i]
            if L[i] < min_:
                min_ = L[i]
        L.remove(max_)
        result.append(max_)
        L.remove(min_)
        result.append(min_)
    for i in range(10):
        print(result[i], end=' ')
    print()
