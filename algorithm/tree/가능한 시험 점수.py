import sys
sys.stdin = open('가능한 시험 점수.txt', 'r')
T = int(input())
for t in range(1, T + 1):
    print(f'#{t}', end=" ")
    N = int(input())
    arr = list(map(int, input().split()))

    results = [0] # 전부 틀린 경우 0 저장
    for i in range(N): # 전체 문제 index
        temp = [] # 새로 계산된 배점을 results에 직접 넣으면 무한루프 발생하므로 temp 생성
        for result in results: # 이전까지 계산된 배점 경우의 수
            temp.append(result + arr[i]) # 이전 경우의 수에 재 문제 더하기
        results = results + temp # temp에 저장된 새로운 경우의 수를 results에 더하기
        results = list(set(results)) # set을 이용해 중복 제거(if문 사용보다 메모리 절약됨)

    print(len(results))
