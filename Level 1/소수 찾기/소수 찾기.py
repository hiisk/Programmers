def solution(n):
    answer = [False, False]+[True]*(n-1)
    for i in range(int(n**0.5)+1):
        if answer[i] == True:
            for j in range(2*i, n+1, i):
                answer[j] = False
    return sum(answer)