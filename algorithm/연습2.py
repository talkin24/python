arr = [-3, 3, -9, 6, 7, -6, 1, 5, 4, 2]

n = len(arr)

cnt = 0
for i in range(1<<n):
    subset = 0
    for j in range(n+1):
        if i & (1<<j):
            subset += arr[j]
    if subset == 0:
        cnt += 1
print(cnt)