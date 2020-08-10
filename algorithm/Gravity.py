data = [7, 4, 2, 0, 0, 6, 0, 7, 0]

def gapCheck(data):
    gaps = []
    for i in range(len(data)):
        height = len(data) - (i+1)
        for j in range(1, data[i]+1):
            count = 0
            for d in data[i+1:]:
                if d >= j:
                    count += 1
            gaps.append(height - count)
    return max(gaps)

print(gapCheck(data))


# 교수님 솔루션
data = [7, 4, 2, 0, 0, 6, 0, 7, 0]
result = 0
maxHeight = 0
for i in range(len(data)):
    #i의 최대 낙차 값은 len(data) - (i+1) : 9 - 1 = 9
    #i이후의 모든 행을 검사한다.
    maxHeight = len(data) - (i + 1)
    for j in range(i+1, len(data), 1): # 아래 행이 i행보다 상자가 많을 때, 최대 낙차 값을 1 감소시킴
        if data[i] <= data[j]:
            maxHeight -= 1
    if result < maxHeight:
        result = maxHeight
print(result)

