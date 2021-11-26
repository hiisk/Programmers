def solution(n):
    answer = [0,1,1]
    if n>2:
        for i in range(2, n):
            answer.append(answer[i-1]+answer[i])

    return answer[n]%1234567