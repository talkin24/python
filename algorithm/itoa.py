def itoa(num):
    arr = []
    x = num # 몫
    y = 0 # 나머지
    while x:
        y = x % 10
        x = x // 10
        arr.append(chr(y + ord('0')))
        # arr.append(y
    arr.reverse()
    str = "".join(arr)
    return str
    # return arr


x = 123
print(x, type(x))
str = itoa(x)
print(str, type(str))