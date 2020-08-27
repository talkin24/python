import sys

sys.stdin = open("괄호검사.txt", "r")

tests = int(input())
for t in range(1, tests + 1):
    print(f"#{t}", end=" ")
    text = input()
    brackets_left = ["(", "{"]
    brackets_right = [")", "}"]
    def check(text):
        stack = [[0]]
        for char in text:
            if char not in (brackets_left + brackets_right):
                pass
            elif char in brackets_left:
                stack.append(char)
            elif char == brackets_right[0]:
                if brackets_left[0] == stack[-1]:
                    stack.pop()
                else:
                    return 0
            elif char == brackets_right[1]:
                if brackets_left[1] == stack[-1]:
                    stack.pop()
                else:
                    return 0
        if len(stack) == 1:
            return 1
        else:
            return 0
    print(check(text))
