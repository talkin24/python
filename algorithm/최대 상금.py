import sys
sys.stdin = open("최대 상금.txt", "r")

import itertools
import copy
def swap(array, index):
    array[index[0]], array[index[1]] = array[index[1]], array[index[0]]
    return array

T = int(input())
for t in range(1, T + 1):
    print(f'#{t}', end=' ')

    info, n = map(int, input().split())


    array = list(map(int, list(str(info))))

    combs = list(itertools.combinations([a for a in range(len(array))], 2))
    all_combs = list(itertools.combinations_with_replacement(combs, n))
    print(all_combs)

    # all_combs2 = []
    #
    # m = 0
    # while m < n:
    #     m += 1
    #     all_combs2.append(combs[j])
    #
    # combs_list = []
    # for _ in range(n):
    #     for i in range(len(combs)):
    #         combs_list.append(combs[i])

    # def combinations_with_replacement2(array, results, n):
    #     if n == 0:
    #         print(results)
    #     else:
    #         n -= 1
    #         for result in results:
    #             for a in array:
    #                 if a not in result:
    #                     result.append(a)
    #                 else:
    #                     result.remove
    #         combinations_with_replacement2(array, )
    for i in range(len(combs)):
        for j in range(len(combs)):
            all_combs2.append([combs[i], combs[j]])
    print(all_combs2)

    def a(combs, result, n):
        for i in range(len(combs)):


    max_val = sorted(array, reverse=True)
    min_val = sorted(array)

    for exs in all_combs:
        new_array = copy.deepcopy(array)
        for ex in exs:
            swap(new_array, ex)
            print(new_array)
        if new_array == max_val:
            result = new_array
            break
        elif new_array >= min_val:
            min_val = new_array
        result = min_val

    print(int(''.join(list(map(str, result)))))

    if t == 5:
        break




