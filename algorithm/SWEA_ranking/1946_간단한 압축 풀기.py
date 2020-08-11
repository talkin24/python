import sys
sys.stdin = open("1946_간단한 압축 풀기.txt", "r")
testcase = int(sys.stdin.readline())
# testcase = int(input())

for t in range(1, testcase + 1):
    print(f'#{t}', end='\n')
    N = int(sys.stdin.readline())
    # N = int(input())

    L = []
    for i in range(N):
        a, b = sys.stdin.readline().split()
        # a, b = input().split()
        texts = (a,b)
        L.append(texts)

    cnt = 0
    for texts in L:
        for i in range(int(texts[1])):
            cnt += 1
            print(texts[0], end='')
            if cnt == 10:
                print()
                cnt = 0
    print()
