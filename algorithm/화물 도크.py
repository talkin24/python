'''
3
5
20 23
17 20
23 24
4 14
8 18
10
14 23
2 19
1 22
12 24
21 23
6 15
20 24
1 4
6 15
15 16
15
18 19
2 7
11 15
13 16
23 24
2 14
13 22
20 23
13 19
7 15
5 21
20 24
16 22
17 21
9 24
'''

def find(array, i, cnt):
    # global cnt
    if i == len(array) - 1:
        results.append(cnt)
    for j in range(len(array[i:])):
        if array[i][1] <= array[i + j][0]:
            print(array[i][1])
            print(array[i+j][0])
            cnt += 1
            find(array, i + j, cnt)
            # break

def find2(array, cnt):
    if len(array) == 1:
        results.append(cnt)
        print(cnt)

    for i in range(len(array)):
        cnt = 1
        for j in range(len(array[i:])):
            if array[i][1] <= array[i + j][0]:
                print(array[i][1])
                print(array[i + j][0])
                cnt += 1
                find2(array[i + j:], cnt)

        # results.append(cnt)
        # print(cnt)



T = int(input())
for t in range(1, T + 1):
    print(f'#{t}', end=' ')

    N = int(input())
    array = [list(map(int, input().split())) for _ in range(N)]
    new_array = sorted(array)
    print(new_array)
    cnt = 1
    results = []
    # find(new_array, 0, cnt)
    # print(results)
    find2(new_array, cnt)
    print(results)
    print(max(results))



