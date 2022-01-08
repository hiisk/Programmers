from fractions import gcd 

def solution(arr):
    answer = (arr[0]*arr[1])/gcd(arr[0],arr[1])

    for i in range(2,len(arr)):
        answer = (answer * arr[i])/gcd(answer,arr[i])

    return answer