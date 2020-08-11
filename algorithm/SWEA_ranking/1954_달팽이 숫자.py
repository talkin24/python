import sys
sys.stdin = open("1954_달팽이 숫자.txt", "r")
testcase = int(sys.stdin.readline())
# testcase = int(input())

for t in range(1, testcase + 1):
    print(f'#{t}', end='\n')

    N = int(sys.stdin.readline())
    # N = int(input())
    
    snail = [[0 for _ in range(N)] for _ in range(N)]
    
    DX = [0, 1, 0, -1]
    DY = [1, 0, -1, 0]
    
    x, y, idx = 0, 0, 0
    for n in range(1, N**2+1):
        snail[x][y] = n
        dx, dy = DX[idx], DY[idx]
        if x + dx not in range(N) or y + dy not in range(N) or snail[x+dx][y+dy] != 0:
            idx = (idx + 1) % 4  
        dx, dy = DX[idx], DY[idx]          
        x, y = x + dx, y + dy

        
    for row in snail:
        for number in row:
            print(number, end=' ')
        print()


    