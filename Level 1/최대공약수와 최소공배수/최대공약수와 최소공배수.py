import math
def solution(n, m):
    result = math.gcd(n,m)
    answer = [result, n*m/result]
    return answer