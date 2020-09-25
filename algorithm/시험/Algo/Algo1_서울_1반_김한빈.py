T = int(input())    # 테스트 케이스 입력
for t in range(1, T + 1):
    print(f'#{t}', end=" ")
    N, M, K = map(int, input().split())     # N, M, K 입력
    arr = [list(map(int, input().split())) for _ in range(N)]       # 행렬 입력, N행만큼 반복하여 N by M 행렬 생성

    outside = []    # 구멍뚫리지 않은 도넛 면적의 합 저장할 리스트(각 좌표별)
    for i in range(N - K + 1):  # 구멍 뚫리지 않은 도넛의 경우, K by K 넓이의 면적이므로 좌표의 범위를 다음과 같이 설정한다.
        for j in range(M - K + 1):
            subsum = 0  # 각 좌표별 부분합
            for dr in range(K): # 상하좌우로 K 면적만큼 더한다
                for dc in range(K):
                    subsum += arr[i + dr][j + dc]
            outside.append(subsum) # 부분합 저장

    inside = []     # 도넛 내부 구멍 뚫어야 하는 부분 면적 합 저장할 리스트
    for i in range(1, N - K + 2):   # 구멍은 전체 도넛 면적보다 1작으므로 1에서 시작.
        for j in range(1, M - K + 2):
            subsum = 0
            for dr in range(K - 2): # 상하좌우 K - 2 면적만큼 더한다
                for dc in range(K - 2): # 도넛 굵기가 1이므로
                    subsum += arr[i + dr][j + dc]
            inside.append(subsum)
    result = []
    for i in range(len(outside)):
        result.append(outside[i] - inside[i]) # 전체 면적 - 구멍 면적
    print(max(result) - min(result))    # 최댓값 - 최솟값

