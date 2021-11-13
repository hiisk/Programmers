def solution(n):
    
    tmp = sorted(str(n),reverse = True)
    
    answer = ''
    
    for i in range(len(tmp)):
        answer += tmp[i]
    
    return int(answer)