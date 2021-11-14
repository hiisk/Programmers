def solution(board, moves):
    answer = 0
    tmp = []
    for i in range(len(moves)):
        for j in range(len(board)):
            if board[j][moves[i]-1] != 0:
                tmp.append(board[j][moves[i]-1])
                if len(tmp) > 1 and tmp[-1] == tmp[-2]:
                    answer +=2
                    del tmp[-2:]
                board[j][moves[i]-1] = 0
                break


    return answer