def solution(board, moves):
    answer = 0
    basket = []
    for move in moves:
        m = int(move) - 1
        for r in range(len(board)):
            if board[r][m] != 0:
                basket.append(board[r][m])
                board[r][m] = 0
                if len(basket) >= 2:
                    if basket[-1] == basket[-2]:
                        basket.pop()
                        basket.pop()
                        answer += 2
                break
    return answer

'''
[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
[1,5,3,5,1,2,1,4]
'''

board = list(map(int, input().replace("[", "").replace("]", "").split(",")))
N = int(len(board)**(1/2))
arr = [board[i:i+5]for i in range(0, len(board), 5)]
moves = list(map(int, input().replace("[", "").replace("]", "").split(",")))
print(solution(arr, moves))
