def solution(answers):
    answer = []

    su_1 = [1, 2, 3, 4, 5]
    su_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    su_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    su_1_c = 0
    su_2_c = 0
    su_3_c = 0

    for i in range(len(answers)):
        if answers[i] == su_1[i%5]:
            su_1_c +=1
        if answers[i] == su_2[i%8]:
            su_2_c +=1
        if answers[i] == su_3[i%10]:
            su_3_c +=1

    max_stu = max(su_1_c, su_2_c, su_3_c)
    if max_stu == su_1_c: answer.append(1)
    if max_stu == su_2_c: answer.append(2)
    if max_stu == su_3_c: answer.append(3)

    return answer