import sys

sys.stdin = open("종이붙이기.txt", "r")

testcases = int(input())
for t in range(1, testcases + 1):
    print(f"#{t}", end=" ")

    N = int(input())

    stack = [0, 1, 3]
    def paper(n):
        n = n/10
        k = 3
        while n != k - 1:
            stack.append(stack[k - 1] + 2 * stack[k - 2])
            k += 1
        return stack[int(n)]
    print(paper(N))