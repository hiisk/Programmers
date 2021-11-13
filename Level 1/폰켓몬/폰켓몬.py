from collections import Counter

def solution(nums):
    answer = 0
    cnt = Counter(nums)
    answer = len(cnt.most_common(len(nums)//2))
    return answer