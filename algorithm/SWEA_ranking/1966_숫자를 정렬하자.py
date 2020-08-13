import sys
sys.stdin = open("1966_숫자를 정렬하자.txt", "r")
testcase = int(sys.stdin.readline())
# testcase = int(input())

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)

for t in range(1, testcase + 1):
    print(f'#{t}', end=' ')
    N = int(sys.stdin.readline())
    # N = int(input())
    arr = list(map(int, sys.stdin.readline().split()))
    # arr = list(map(int, input().split()))

    for i in quick_sort(arr):
        print(i, end=" ")
    print()
    