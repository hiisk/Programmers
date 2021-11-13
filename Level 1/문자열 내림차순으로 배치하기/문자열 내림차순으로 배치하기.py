def solution(s):
    answer =''
    s = list(s)
    for i in range(len(s)):
        s[i] = ord(s[i])
    s = sorted(s, reverse=True)

    for i in range(len(s)):
        answer+= chr(s[i])
    return answer