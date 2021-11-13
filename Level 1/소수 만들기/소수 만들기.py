from itertools import combinations 

def solution(nums):
    answer = 0
    tmp = list(combinations(nums,3))
    tmp_list = []
    for i in range(len(tmp)):
        tmp_sum = sum(tmp[i])
        for j in range(2, tmp_sum):
            if tmp_sum%j == 0 :
                tmp_list.append(tmp_sum)
                break
        answer = len(tmp) - len(tmp_list)
    return answer