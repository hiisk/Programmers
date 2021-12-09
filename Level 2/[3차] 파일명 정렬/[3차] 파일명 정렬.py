def solution(files):
    answer = []
    str = []

    for s in files:
        HEAD=''
        for char in s:
            if char.isdigit():
                break
            HEAD+=char

        NUMBER=''        
        for char in s[len(HEAD):]:
            if not char.isdigit():
                break
            NUMBER+=char

        str.append([HEAD.lower(),int(NUMBER),s])

    s_list = sorted(str, key=lambda x:(x[0],x[1]))
    for i in s_list:
        answer.append(i[2])
    return answer