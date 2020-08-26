def BruteForce(p, t):
    i, j = 0, 0
    while i < len(p) and j < len(t):
        if p[i] != t[j]:
            j = j - i
            i = -1
        i += 1
        j += 1
    if i == len(p): return j - len(p)
    else: return - 1


def BruteForce2(text, pattern):
    for i in range(len(text) - len(pattern) + 1):
        cnt = 0
        for j in range(len(pattern)):
            if text[i+j] != pattern[j]:
                break
            else: cnt += 1
        if (cnt >= len(pattern)): return i
    return -1

p = "is" # 찾을 패턴
t = "This is a book~!" # 전체 텍스트

print(BruteForce(p, t))
print(BruteForce2(t, p))


text = "TTTTAACCA"
pattern = "AA"

print(BruteForce(pattern, text))
print(BruteForce2(text, pattern))