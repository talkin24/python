str = "algorithm"
arr = []
for c in str:
    arr.append(c)

for i in range(len(arr)//2 ):
    temp = 0
    temp = arr[i]
    arr[i] = arr[len(arr) - 1 - i]
    arr[len(arr) - 1 - i] = temp

str_reverse = "".join(arr)
print(str_reverse)

# 교수 솔루션
def str_rev(str):
    # str -> list
    arr = list(str)
    # swap
    for i in range(len(arr)//2):
        arr[i], arr[len(arr) - 1 - i] = arr[len(arr) - 1 - i], arr[i]
    # list -> str
    str = "".join(arr)
    return str
str = 'algorithm'
str1 = str_rev(str)
print(str1)