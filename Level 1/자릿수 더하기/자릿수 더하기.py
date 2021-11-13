def solution(n):
    answer = 0
    a = list(str(n))
    for i in range(len(a)):
        answer+=int(a[i])
    return answer