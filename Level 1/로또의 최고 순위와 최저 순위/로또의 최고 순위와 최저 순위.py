def solution(lottos, win_nums):
    tmp_1 = 0
    tmp_2 = 0
    answer = []

    for i in range(len(win_nums)):
        if lottos[i] in win_nums:
            tmp_1 +=1
        elif lottos[i] == 0:
            tmp_2 +=1
    if tmp_1 > 1:
        tmp_1 = 7 - tmp_1
    else:
        tmp_1 = 6

    if tmp_2 < 6 :
        tmp_2 = tmp_1 - tmp_2
    else:
        tmp_2 = 1

    answer.append(tmp_2)
    answer.append(tmp_1)

    return answer