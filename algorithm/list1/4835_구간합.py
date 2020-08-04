import sys
sys.stdin = open("4835_구간합.txt", "r")

testcase = int(sys.stdin.readline())

for t in range(1,testcase+1):
    print(f'#%s' %t, end=' ')
    N, M = list(map(int, sys.stdin.readline().split()))
    L = list(map(int, sys.stdin.readline().split()))

# testcase = int(input())
# for t in range(1,testcase+1):
#     print(f'#{t}', end=' ')
#     N, M = list(map(int, input().split()))
#     L = list(map(int, input().split()))

    sums = []
    for i in range(len(L)- (M-1)):
        sum_part = 0
        for j in range(0, M):
            sum_part += L[i+j]
        sums.append(sum_part)

    max_sum, min_sum = sums[0], sums[0]
    for s in sums:
        if s > max_sum:
            max_sum = s
    for s in sums:
        if s < min_sum:
            min_sum = s
    print(max_sum - min_sum)
