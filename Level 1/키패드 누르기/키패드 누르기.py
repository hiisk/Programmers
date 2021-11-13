def solution(numbers, hand):
    answer = ''
    key_dict = {1:(0,0),2:(0,1),3:(0,2),
                4:(1,0),5:(1,1),6:(1,2),
                7:(2,0),8:(2,1),9:(2,2),
                '*':(3,0),0:(3,1),'#':(3,2)} 

    L = [1,4,7]
    R = [3,6,9]
    temp_l = '*'
    temp_r = '#'
    for number in numbers:
        if number in L:
            answer += 'L'
            temp_l = number
        elif number in R:
            answer += 'R'
            temp_r = number
        else:
            curPos = key_dict[number]
            lPos = key_dict[temp_l]
            rPos = key_dict[temp_r]
            ldist = abs(curPos[0]-lPos[0]) + abs(curPos[1]-lPos[1])
            rdist = abs(curPos[0]-rPos[0]) + abs(curPos[1]-rPos[1])

            if ldist < rdist:
                answer += 'L'
                temp_l = number
            elif ldist > rdist:
                answer += 'R'
                temp_r = number
            else:
                if hand == 'left':
                    answer += 'L'
                    temp_l = number
                else:
                    answer += 'R'
                    temp_r = number

    return answer