T = int(input())
for t in range(1, T+1):
    # test case number
    print(f"#{t}", end=" ")
    # N(배열의 크기), M(첫번째 입력값), D(변경 값) 입력 받기
    N, M, D = map(int, input().split())

    # 빈 array 생성
    arr = [[0] * N for _ in range(N)]

    # 대각선은 중앙으로부터 일정하게 D만큼 증가(D 음수일 경우 감소)하므로 대각선을 따라 규칙적으로 입력
    for dr in range(N//2 + 1):
        # 왼쪽 상단 대각선
        arr[0 + dr][0 + dr] = M + (N//2) * D - D * dr
        # 우측 상단 대각선
        arr[0 + dr][N-1 - dr] = M + (N//2) * D - D * dr
        # 좌측 하단 대각선
        arr[N-1 - dr][0 + dr] = M + (N//2) * D - D * dr
        # 우측 하단 다각선
        arr[N-1 - dr][N-1 - dr] = M + (N//2) * D - D * dr

    # 각 row별로 입력된 값들 사이에 동일한 값을 입력한다. ex) [0, 9, 0, 0, 0, 9, 0] -> [0, 9, 9, 9, 9, 9, 0]
    for r in range(len(arr)):
        temp = []
        for c in range(len(arr[0])):
            if arr[r][c] != 0: # 0이 아닌 값의 좌표 저장
                temp.append(c)
        s = temp[0] + 1 # 0이 아닌 값의 시작(start)
        e = temp[-1] # 0이 아닌 좌표의 끝(end)
        for i in range(s,e):
            arr[r][i] = arr[r][e] # 각 좌표에 (대각선 생성시 입력된) 값 입력

    # 가로는 다 채웠으나, 세로가 여전히 비어있음
    # 각 row별로 값이 비어있다면 값이 존재하는 (바로 옆의 값 + D)를 입력한다.
    for r in arr:
        for dc in range(N//2 + 1): # 오른쪽만 확인
            if r[N//2] != 0 and r[N//2 + dc] == 0: # 중앙이 0이 아니고 오른쪽 값이 0일 때
                r[N // 2 + dc] = r[N//2 + dc - 1] + D # 0인 값의 왼쪽 값에서 D를 더한 값을 대입
        for dc in range(N//2 + 1): # 왼쪽만 확인
            if r[N//2] != 0 and r[N//2 - dc] == 0: # 중앙이 0이 아니고 왼쪽 값이 0일 때
                r[N // 2 - dc] = r[N//2 - dc + 1] + D # 0인 값의 오른쪽 값에서 D를 더한 값을 대입

    # 각 행의 합을 출력
    for r in arr:
        print(sum(r), end=" ")
    print()