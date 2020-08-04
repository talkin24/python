import sys
sys.stdin = open("4834_숫자카드.txt", "r")

testcase = int(sys.stdin.readline())

for t in range(1,testcase+1):
    print(f'#%s' %t, end=' ')
    n = int(sys.stdin.readline())
    cards = sys.stdin.readline()
# testcase = int(input())
# for t in range(1,testcase+1):
#     print(f'#{t}', end=' ')
#     n = int(input())
#     cards = input()

    count = {}
    i = 0
    for card in cards[:n]:
            count[card] = 0
    for card in cards[:n]:
        count[card] += 1
    max_value = 0
    max_key = ''
    keys = list(count.keys())
    for i in range(len(keys)):
        if count[keys[i]] > max_value:
            max_value = count[keys[i]]
            max_key = keys[i]
        elif count[keys[i]] == max_value:
            if int(keys[i]) > int(max_key):
                max_key = keys[i]
                max_value = count[keys[i]]
    print(max_key, max_value)
