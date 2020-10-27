import sys
sys.stdin = open("암호코드 스캔.txt", "r")

hex2dec = {
    '0': "0000",
    '1': "0001",
    '2': "0010",
    '3': "0011",
    '4': "0100",
    '5': "0101",
    '6': "0110",
    '7': "0111",
    '8': "1000",
    '9': "1001",
    'A': "1010",
    'B': "1011",
    'C': "1100",
    'D': "1101",
    'E': "1110",
    'F': "1111"
}
def convert2(num): # 16진수 -> 2진수
    return hex2dec.get(num)

def div_with_min(arr): # 최솟값으로 나누기(비율확인)
    min_value = min(arr)
    new_arr = []
    for a in arr:
        new_arr.append(int(a / min_value))
    return new_arr

def convert_pw(arr): # 암호 변환
    arr = str(arr)
    dict = {
        '[2, 1, 1]': 0,
        '[2, 2, 1]': 1,
        '[1, 2, 2]': 2,
        '[4, 1, 1]': 3,
        '[1, 3, 2]': 4,
        '[2, 3, 1]': 5,
        '[1, 1, 4]': 6,
        '[3, 1, 2]': 7,
        '[2, 1, 3]': 8,
        '[1, 1, 2]': 9
    }
    return dict.get(arr)


T = int(input())
for t in range(1, T + 1):

    print(f'#{t}', end=' ')

    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    new_arr = []
    for row in arr:
        new_row = ''
        for num in row:
            new_row += convert2(num)
        new_arr.append(new_row)


    ratios_set = []
    for row in new_arr:
        switch = 0
        code = []
        ratios = []


        for i in range(len(row)):
            if len(code) == 3:
                code = div_with_min(code)
                ratios.append(convert_pw(code))
                code = []
            if len(ratios) == 8:
                if ratios not in ratios_set:
                    ratios_set.append(ratios)
                ratios = []

            if row[i] == '1' and switch == 0: # 처음으로 1을 만나면
                switch = 1                  # switch 키고
                cnt = 1                     # 숫자 세기
            elif row[i] == row[i - 1] and switch >= 1:   # switch 켜져있고, 이전 것과 값이 동일하면
                cnt += 1                                 # cnt 증가
            elif row[i] != row[i - 1] and 1<= switch <= 2:
                code.append(cnt)
                cnt = 1
                switch += 1
            elif row[i] != row[i - 1] and switch == 3:
                code.append(cnt)
                switch = 0


        if len(ratios) > 0 and (ratios not in ratios_set):
            ratios_set.append(ratios)

    result = 0
    for sols in ratios_set:
        if ((sols[0] + sols[2] + sols[4] + sols[6]) * 3 + (sols[1] + sols[3] + sols[5]) + sols[7]) % 10 == 0:
            result += sum(sols)
    print(result)








