import sys
sys.stdin = open("4839_이진탐색.txt", "r")

testcase = int(sys.stdin.readline())
# testcase = int(input())
for t in range(1,testcase+1):
    print(f'#{t}', end=' ')
    P, A, B = list(map(int, sys.stdin.readline().split()))
    # P, A, B = list(map(int, input().split()))

    tgts = [A, B]
    cnts = []
    for t in tgts:
        l, r, c, cnt = 1, P, -1, 0
        while c != t:
            c = int((l+r)/2)
            if t < c:
                r = c
                cnt += 1
            elif t > c:
                l = c
                cnt += 1
        cnts.append(cnt)

    if cnts[0] < cnts[1]:
        print('A')
    elif cnts[0] > cnts[1]:
        print('B')
    else:
        print(0)

