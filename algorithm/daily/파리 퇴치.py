import sys
sys.stdin = open("파리 퇴치.txt", "r")

testcase = int(sys.stdin.readline())
# testcase = int(input())
for t in range(1,testcase+1):
    print(f'#{t}', end=' ')
    N, M = list(map(int, sys.stdin.readline().split()))
    # N, M = list(map(int, input().split()))
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    # arr = [list(map(int, input().split())) for _ in range(N)]

    max_sum = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            sub_sum = 0
            for m in range(M):
                for n in range(M):
                    sub_sum += arr[i+m][j+n]
            if sub_sum > max_sum:
                max_sum = sub_sum
    print(max_sum)