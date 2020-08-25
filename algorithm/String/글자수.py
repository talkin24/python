import sys

sys.stdin = open("글자수.txt.", "r")
testcase = int(sys.stdin.readline())
# testcase = int(input())
for t in range(1, testcase + 1):
    print(f'#{t}', end=" ")

    str1, str2 = sys.stdin.readline()[:-1], sys.stdin.readline()[:-1]
    # str1, str2 = input(), input()

    dic = {}
    for char in str1:
        dic[char] = str2.count(char)

    print(max(dic.values()))