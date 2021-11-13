def solution(arr):
    a = min(arr)

    answer = arr
    if answer[0] == 10:
        answer[0] = -1
    else:
        answer.remove(a)
    return answer