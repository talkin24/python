def solution(participant, completion):
    # 1
    # answer = ''
    # participant.sort()
    # completion.sort()
    # for i in range(len(completion)):
    #     if participant[i] != completion[i]:
    #         answer = participant[i]
    #         break
    #     answer = participant[-1]
    # return answer

    # 2
    # answer = ''
    # temp = 0
    # dic = {}
    # for p in participant:
    #     dic[hash(p)] = p
    #     temp += hash(p)
    # for c in completion:
    #     temp -= hash(c)
    # answer = dic[temp]
    # return answer

    # 3
    import collections
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

participant = ['mislav', 'stanko', 'mislav', 'ana']
completion = ['stanko', 'ana', 'mislav']
print(solution(participant, completion))
