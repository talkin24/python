# 최소합만 지원(heapq)
import heapq
heap1 = [7, 2, 5, 3, 4, 6] # List
print(heap1)
heapq.heapify(heap1)
print(heap1)
heapq.heappush(heap1, 1)
print(heap1)
while heap1:
    print(heapq.heappop(heap1), end =" ")
print()
##########################################
# 음수를 붙이면 최댓값도 뽑아낼 수 있음
temp = [7, 2, 5, 3, 4, 6]
heap2 = []
for i in range(len(temp)):
    # heapq.heappush(heap2, (-temp[i], temp[i]))
    heapq.heappush(heap2, (-temp[i]))
print(heap2)
# heapq.heappush(heap2, (-1, 1))
heapq.heappush(heap2, (-1))
print(heap2)
while heap2:
    print(heapq.heappop(heap2) * -1, end = " ")
    # print(heapq.heappop(heap2[0]) * -1, end = " ")
print(heap2)