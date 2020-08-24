def atoi(str):
    value = 0
    for i in range(len(str)):
        c = str[i]
        # 0 ~ 9
        if c >= '0' and c <= '9':
            digit = ord(c) - ord('0') # c - '0'
        else:
            break
        value = value * 10 + digit
    return value


a = "1237"
print(type(a))
b = atoi(a)
print(type(b))