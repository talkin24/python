import sys

sys.stdin = open("GNS.txt", "r")
# testcase = int(sys.stdin.readline())
testcase = int(input())

for t in range(1, testcase + 1):
    print(f'#{t}', end=' ')

    # _, length = sys.stdin.readline().split()
    _, length = input().split()
    length = int(length)
    # arr = list(sys.stdin.readline().split())
    arr = list(input().split())

    dic = {"ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4, "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9}

    arr_num = [dic[k] for k in arr]
    arr_num_sorted = sorted(arr_num)

    arr_sorted = []
    for num in arr_num_sorted:
        for k, v in dic.items():
            if v == num:
                print(k, end=" ")
    print()



