def solution(a, b):
    answer = ''
    result = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    plus = 0
    for i in range(1, a):
        if i in (1,3,5,7,8,10,12):
            plus += 31
        elif i in (4,6,9,11):
            plus += 30
        elif i == 2:
            plus += 29
    plus += b-1
    answer = result[plus%7]    
    return answer