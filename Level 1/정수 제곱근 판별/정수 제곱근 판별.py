def solution(n):
    
    if n**(1/2)%1 ==0:
        n = n**(1/2)
        answer = (n+1)**2
    else:
        answer = -1
    return answer