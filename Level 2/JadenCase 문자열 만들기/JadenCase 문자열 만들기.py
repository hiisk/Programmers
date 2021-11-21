def solution(s):
    answer = ''
    tmp = s.split(' ')
    for i in range(len(tmp)):
        tmp[i] = tmp[i].capitalize()
    
    answer = ' '.join(tmp)
    return answer