import sys

sys.stdin = open("재미있는 오셀로 게임.txt", "r")
T = int(input())
for t in range(1, T + 1):
    print(f"#{t}", end=" ")
    N, M = input().split()
    N, M = int(N), int(M)

    acts = [list(map(int, input().split())) for _ in range(M)]
    b, w = 0, 0
    board = [[0] * (N + 2) for i in range(N + 2)] # add padding
    board[N // 2][N // 2 + 1] = board[N // 2 + 1][N // 2] = 1
    board[N // 2][N // 2] = board[N // 2 + 1][N // 2 + 1] = 2
    drs = [-1, -1,  0, 1, 1,  1,  0, -1]
    dcs = [ 0,  1,  1, 1, 0, -1, -1, -1]
    for act in acts:
        for d in range(len(drs)):
            c = act[0]
            r = act[1]
            board[r][c] = act[2]
            if (board[r + drs[d]][c + dcs[d]] != 0) and (board[r + drs[d]][c + dcs[d]] != act[2]):
                r0 = r + drs[d]
                c0 = c + dcs[d]
                while board[r + drs[d]][c + dcs[d]] != act[2]:
                    if board[r + drs[d]][c + dcs[d]] == 0:
                        break
                    else:
                        r += drs[d]
                        c += dcs[d]
                        if board[r + drs[d]][c + dcs[d]] == act[2]:
                            while board[r0][c0] != act[2]:
                                board[r0][c0] = act[2]
                                r0 += drs[d]
                                c0 += dcs[d]
                            break
    ws, bs = 0, 0
    for row in board:
        ws += list(row).count(1)
        bs += list(row).count(2)
    print(ws, bs)