import sys

sys.stdin = open("괄호 짝짓기.txt", "r")

for t in range(10):
    print(f"#{t+1}", end=" ")

    n = int(input())
    brackets = input()

    stack1, stack2, stack3, stack4 = 0, 0, 0, 0
    # front = ["(", "{", "[", "<"]
    # back = [")", "}", "]", ">"]
    for bracket in brackets:
        if bracket == "(":
            stack1 += 1
        elif bracket == ")":
            stack1 -= 1
        if bracket == "{":
            stack2 += 1
        elif bracket == "}":
            stack2 -= 1
        if bracket == "[":
            stack3 += 1
        elif bracket == "]":
            stack3 -= 1
        if bracket == "<":
            stack4 += 1
        elif bracket == ">":
            stack4 -= 1
    if stack1 == stack2 == stack3 == stack4 == 0:
        result = 1
    else:
        result = 0

    print(result)