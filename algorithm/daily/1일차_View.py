testcase = 10

for t in range(1,testcase+1):
    print(f'#{t}', end=' ')
    n = int(input())
    buildings = list(map(int, input().split()))

    result = 0
    for i in range(2, len(buildings)-2):
        around_building = [buildings[i - 2], buildings[i - 1], buildings[i + 1], buildings[i + 2]]
        if buildings[i] < max(around_building):
            pass
        else:
            result += buildings[i] - max(around_building)

    print(result)


