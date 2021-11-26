def solution(n):
    answer = 0
    value = 0
    for i in range(1, n+1):
        for j in range(i, n+1):
            value+=j
            if value == n:
                answer+=1
            elif value > n:
                value = 0
                break
    return answer