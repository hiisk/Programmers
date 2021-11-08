def solution(phone_number):
    a=''
    for i in range(len(phone_number)-4):
        a = a +"*"
    a +=phone_number[-4:]
    answer = a
    return answer