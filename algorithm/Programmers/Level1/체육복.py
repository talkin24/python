# def solution(n, lost, reserve):
    # if len(reserve) == 1:
    #
    # answer = 0
    # reserve_later = []
    # for r in reserve:
    #     if ((r - 1) in lost) and ((r + 1) in lost):
    #         reserve_later.append(r)
    #     elif (r - 1) in lost:
    #         lost.remove(r - 1)
    #         reserve.remove(r)
    #     elif (r + 1) in lost:
    #         lost.remove(r + 1)
    #         reserve.remove(r)
    # for r in reserve
    # answer = n - len(lost)
    # return answer

# def solution(n, lost, reserve):
#     answer = 0
#     reserve_later = []
#     for r in reserve:
#         if r in lost:
#             lost.remove(r)
#             reserve.remove(r)
#         if ((r - 1) in lost) and ((r + 1) in lost):
#             reserve_later.append(r)
#         elif (r - 1) in lost:
#             lost.remove(r - 1)
#             reserve.remove(r)
#         elif (r + 1) in lost:
#             lost.remove(r + 1)
#             reserve.remove(r)
#
#     answer = n - len(lost)
#     return answer

# def solution(n, lost, reserve):
#     if len(set(lost + reserve)) != len(lost + reserve):
#         for a in lost:
#             if a in reserve:
#                 lost.remove(a)
#     else:
#         b = 1
#         dic = {}
#         while b == 1:
#             b = 0
#             for a in lost:
#                 if ((a-1) in reserve) and ((a+1) in reserve):
#                     dic[a] = 'B'
#                 elif (a-1) in reserve:
#                     dic[a] = 'L'
#                     b = 1
#                 elif (a+1) in reserve:
#                     dic[a] = 'R'
#                     b = 1
#             for k, v in dic.items():
#                 try:
#                     if v == 'L':
#                         reserve.remove(k - 1)
#                         lost.remove(k)
#                     if v == 'R':
#                         reserve.remove(k + 1)
#                         lost.remove(k)
#                 except:
#                     pass
#             dic = {key:val for key, val in dic.items() if val == 'B'}
#         for k, v in dic.items():
#             if v == 'B':
#                 try:
#                     reserve.remove(k - 1)
#                 except:
#                     reserve.remove(k + 1)
#                 lost.remove(k)
#         return n - len(lost)
    # for k, v in dic.items():
    #     if v == 'B':
    #         try:
    #             reserve.remove(k - 1)
    #         except:
    #             reserve.remove(k + 1)
    #         lost.remove(k)
    # return n - len(lost)

# def solution(n, lost, reserve):
#     for l in lost:
#         if l in reserve:
#             reserve.remove(l)
#             lost.remove(l)
#     lost_picked = [0] * len(lost)
#     for r in reserve:
#             if r - 1 in lost:
#                 lost_picked[lost.index(r - 1)] += 1
#             if r + 1 in lost:
#                 lost_picked[lost.index(r + 1)] += 1
#
#     for i in range(len(lost)):
#         if lost_picked[i] == 1:
#             try:
#                 if (lost[i] - 1) in reserve:
#                     reserve.remove(lost[i] - 1)
#                     lost.remove(lost[i])
#                     lost_picked[i] -= 1
#             except:
#                 pass
#             try:
#                 if (lost[i] + 1) in reserve:
#                     reserve.remove(lost[i] + 1)
#                     lost.remove(lost[i])
#                     lost_picked[i] -= 1
#             except:
#                 pass
#     return n - len(lost) + len([a for a in lost_picked if a == 2])


def solution(n, lost, reserve):
    lost_check = [1] * len(lost)
    reserve_check = [1] * len(reserve)
    for l in lost:
        if l in reserve:
            reserve_check[reserve.index(l)] = 0
            lost_check[lost.index(l)] = 0

    for l in lost:
        if ((l - 1) in reserve) and (reserve_check[reserve.index(l - 1)] != 0) and ((l + 1) not in reserve):
            reserve_check[reserve.index(l - 1)] = 0
            lost_check[lost.index(l)] = 0
        if ((l + 1) in reserve) and (reserve_check[reserve.index(l + 1)] != 0) and ((l - 1) not in reserve):
            reserve_check[reserve.index(l + 1)] = 0
            lost_check[lost.index(l)] = 0

    for l in lost:
        if ((l - 1) in reserve) and (reserve_check[reserve.index(l - 1)] != 0):
            reserve_check[reserve.index(l - 1)] = 0
            lost_check[lost.index(l)] = 0
        elif ((l + 1) in reserve) and (reserve_check[reserve.index(l + 1)] != 0):
            reserve_check[reserve.index(l + 1)] = 0
            lost_check[lost.index(l)] = 0
    lost_num = lost_check.count(1)
    return n - lost_num


n = 5
lost = [2, 4]
reserve = [1, 3, 5]
print(solution(n, lost, reserve))