import sys
sys.stdin = open("1970_쉬운 거스름돈.txt", "r")
testcase = int(sys.stdin.readline())
# testcase = int(input())

for t in range(1, testcase + 1):
    print(f'#{t}', end='\n')
    N = int(sys.stdin.readline())
    # N = int(input())
    
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    changes = [0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(len(money)):
        changes[i] += N // money[i]
        N = N % money[i]

    for change in changes:
        print(change, end=' ')
    print()
        