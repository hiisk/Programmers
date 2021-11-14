def solution(new_id):
    answer = ''
    new_id = list(new_id)
    tmp = new_id.copy()
    for i in range(len(new_id)):
        if new_id[i].isalpha() and new_id[i] != new_id[i].lower():
            tmp[i] = new_id[i].lower()
        if not (new_id[i].isalnum() or new_id[i] == '-' or new_id[i] == '_' or new_id[i] == '.' ):
            tmp[i] = 0

    tmp_5 = []
    for i in range(len(tmp)):
        if tmp[i] != 0 :
            tmp_5.append(tmp[i])
    for i in range(1,len(tmp_5)):
        if tmp_5[i] =='.' and tmp_5[i-1] =='.':
            tmp_5[i-1] = 0

    tmp_2 = []
    for i in range(len(tmp_5)):
        if tmp_5[i] != 0 :
            tmp_2.append(tmp_5[i])
    if tmp_2 == []:
         tmp_2 = ['a']
    if tmp_2[0] =='.':
        for j in range(0, len(tmp_2)):
            if tmp_2[j]== '.':
                tmp_2[j] = 0
            else:
                break


    tmp_3 = []
    for i in range(len(tmp_2)):
        if tmp_2[i] != 0 :
            tmp_3.append(tmp_2[i])
    if tmp_3 == []:
         tmp_3 = ['a']

    tmp_3 = tmp_3[:15]
    if tmp_3[-1] =='.':
        for j in range(1, len(tmp_3)):
            if tmp_3[-j]== '.':
                tmp_3[-j] = 0
            else:
                break

    tmp_4 = []
    for i in range(len(tmp_3)):
        if tmp_3[i] != 0 :
            tmp_4.append(tmp_3[i])
    if tmp_4 == []:
         tmp_4 = ['a']
    if len(tmp_4)<3:
        for i in range(3-len(tmp_4)):
            tmp_4 +=tmp_4[-1]
    print(tmp_4)
    for i in range(len(tmp_4)):
        answer += tmp_4[i]
    return answer