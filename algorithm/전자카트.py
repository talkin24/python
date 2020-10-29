'''
3
3
0 18 34
48 0 55
18 7 0
4
0 83 65 97
82 0 78 6
19 19 0 82
6 34 94 0
5
0 9 26 85 42
14 0 84 31 27
58 88 0 16 46
83 61 94 0 17
40 71 24 38 0
'''

import itertools

T = int(input())
for t in range(1, T + 1):
    print(f'#{t}', end=' ')

    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    li = [a for a in range(2, N + 1)]
    perms = list(itertools.permutations(li, len(li)))

    result = float('inf')
    for perm in perms:
        battery = 0

        battery += arr[0][perm[0] - 1]
        for i in range(len(perm) - 1):
            battery += arr[perm[i] - 1][perm[i + 1] - 1]
        battery += arr[perm[-1] - 1][0]

        if battery <= result:
            result = battery
    print(result)