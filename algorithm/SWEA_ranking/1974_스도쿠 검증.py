import sys
sys.stdin = open("1974_스도쿠 검증.txt", "r")
testcase = int(sys.stdin.readline())
# testcase = int(input())

for t in range(1, testcase + 1):
    print(f'#{t}', end='\n')
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(9) ]
    # arr = [list(map(int, input().split())) for _ in range(9) ]
    
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for r in arr:
        for num in nums:
            if r.count(num) == 0:
                print(0)
                break
    
    for c in range(len(arr[0])):
        column = []
        for r in range(len(arr)):
            column.append(arr[r][c])
        for num in nums:
            if column.count(num) == 0:
                print(0)
                break

    for r in range(len(arr),3):
        for c in range(len(arr),3):
            temp = []
            for dr in range(3):
                for dc in range(3):
                    temp = arr[r+dr][c+dc]
            for num in nums:
                if temp.count(num) == 0:
                    print(0)
                    break
        print(1)


            

        
            
        
