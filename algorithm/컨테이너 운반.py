'''
3
3 2
1 5 3
8 3
5 10
2 12 13 11 18
17 4 7 20 3 9 7 9 20 5
10 12
10 13 14 6 19 11 5 20 11 14
5 18 17 8 9 17 18 4 1 16 15 13
'''
T = int(input())
for t in range(1, T + 1):
    print(f'#{t}', end=' ')

    N, M = map(int, input().split())
    containers = sorted(list(map(int, input().split())), reverse=T)
    trucks = sorted(list(map(int, input().split())), reverse=T)


    moved = 0
    max_value = max(trucks) * 2
    for i in range(len(trucks)):
        for j in range(len(containers)):
            if trucks[i] >= containers[j]:
                moved += containers.pop(j)
                containers.append(max_value)
                break
            else:
                pass
    print(moved)





