import sys
sys.stdin = open("1948_날짜 계산기.txt", "r")
testcase = int(sys.stdin.readline())
# testcase = int(input())

dic = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 
        10:31, 11:30, 12:31}

for t in range(1, testcase + 1):
    print(f'#{t}', end=' ')
    L = list(map(int, sys.stdin.readline().split()))
    # L = list(map(int, input().split()))

    if L[0] == L[2]:
        print(L[3] - L[1] + 1)
    else:
        days = L[3] - L[1] + 1
        for m in range(L[0], L[2]):
            days += dic[m]
        print(days)