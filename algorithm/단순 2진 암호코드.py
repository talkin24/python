import sys
sys.stdin = open("단순 2진 암호코드.txt", "r")
T = int(sys.stdin.readline())

for t in range(1, T + 1):
    print(f'#{t}', end=' ')
    