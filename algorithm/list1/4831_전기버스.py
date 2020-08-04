import sys
sys.stdin = open("4831_전기버스.txt", "r")

testcase = int(sys.stdin.readline())

for t in range(1,testcase+1):
    print(f'#%s' %t, end=' ')
    charge, destination, stop = map(int, sys.stdin.readline().split())
    stops = list(map(int, sys.stdin.readline().split()))

# testcase = int(input())
# for t in range(1,testcase+1):
#     print(f'#{t}', end=' ')
#     charge, destination, stop = map(int, input().split())
#     stops = list(map(int, input().split()))

    stops.append(destination)
    chargeCnt = 0
    loc = 0
    while loc + charge < destination:
        for i in range(len(stops)-1):
            if stops[i+1] - stops[i] > charge:
                chargeCnt = 0
                loc = destination
                break
            if stops[i] <= loc + charge < stops[i+1]:
                loc = stops[i]
                chargeCnt += 1
            else:
                pass
    print(chargeCnt)

