import sys
sys.stdin = open("input.txt", "r")

testcase = int(sys.stdin.readline())

for t in range(1,testcase+1):
    print(f'#%s' %t, end=' ')
    n = int(sys.stdin.readline())
    L = list(map(int, sys.stdin.readline().split()))
