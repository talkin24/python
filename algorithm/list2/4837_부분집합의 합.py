import sys
sys.stdin = open("4837_부분집합의 합.txt", "r")

testcase = int(sys.stdin.readline())
# testcase = int(input())
for t in range(1,testcase+1):
    print(f'#{t}', end=' ')
    N, K = list(map(int, sys.stdin.readline().split()))
    # N, K = list(map(int, input().split()))


    arr = [i for i in range(1,13)]

    cnt = 0
    for i in range(1<<len(arr)):
        sub = []
        for j in range(len(arr)+1):
            if i & (1<<j):
                sub.append(arr[j])
        if (len(sub) == N) & (sum(sub) == K):
           cnt +=1
    print(cnt)
