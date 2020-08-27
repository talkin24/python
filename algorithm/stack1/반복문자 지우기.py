import sys

def rmDuplication(word):
    global length_new
    global length_old
    if length_old == length_new:
        print(length_new)
    else:
        length_old = length_new
        for i in range(len(word) - 1):
            if word[i] == word[i + 1]:
                del word[i]
                del word[i]
                break
        length_new = len(word)
        return rmDuplication(word)

sys.stdin = open("반복문자 지우기.txt", "r")
tests = int(input())
for t in range(1, tests + 1):
    print(f"#{t}", end=" ")
    string = list(input())
    length_old = 0
    length_new = 1
    rmDuplication(string)



