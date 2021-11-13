def solution(n, lost, reserve):
    answer = 0
#     reserve_test = []
#     for i in range(len(reserve)):
#         if reserve[i]-1 != 0 and reserve[i]-1 in lost and reserve[i] not in lost:
#             reserve_test.append(reserve[i]-1)
#         elif reserve[i]+1 <= n and reserve[i]+1 in lost and reserve[i] not in lost:
#             reserve_test.append(reserve[i]+1)
#     reserve_test = list(set(reserve_test))

#     for i in range(len(reserve_test)):
#         if reserve_test[i] in lost:
#             answer+=1
#     answer = answer + n -len(lost)
    reserve_n = list(set(reserve) - set(lost)) 
    lost_n = list(set(lost) - set(reserve)) 
    answer = n - len(lost_n) 
    for i in lost_n: 
        if i - 1 in reserve_n: 
            answer += 1 
            reserve_n.remove(i - 1) 
        elif i + 1 in reserve_n: 
            answer += 1 
            reserve_n.remove(i + 1) 

    return answer