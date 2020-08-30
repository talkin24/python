def solution(answers):
    result = []
    num1 = [1, 2, 3, 4, 5]
    num2 = [1, 3, 4, 5]
    num3 = [3, 1, 2, 4, 5]
    p1 = [num1[i % 5] for i in range(len(answers))]
    p2 = []
    for i in range(len(answers)):
        p2.append(2)
        p2.append(num2[i % 4])
    p3 = []
    for i in range(len(answers)):
        p3.append(num3[i % 5])
        p3.append(num3[i % 5])
    score = {1:0, 2:0, 3:0}
    for i in range(len(answers)):
        if answers[i] == p1[i]:
            score[1] += 1
        if answers[i] == p2[i]:
            score[2] += 1
        if answers[i] == p3[i]:
            score[3] += 1
    first = max(score.values())
    for k, v in score.items():
        if v == first:
            result.append(k)
    result.sort()
    return result

def solution2(answers):
    pattern1 = [1, 2, 3, 4, 5]
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx % len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx % len(pattern2)]:
            score[0] += 1
        if answer == pattern3[idx % len(pattern3)]:
            score[0] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx + 1)
    return result


answers = [1,2,3,4,5]
print(solution(answers))
print(solution2(answers))

