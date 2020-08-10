Array = [[0,1,2,3],
       [4,5,6,7],
       [8,9,10,11]
       ]
n = len(Array)
m = len(Array[0])

for i in range(n):
    for j in range(m):
        print(Array[i][j + (m-1-2*j) * (i % 2)])