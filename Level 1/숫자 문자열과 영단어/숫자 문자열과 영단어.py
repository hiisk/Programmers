def solution(s):
    answer = ''
    if s.isnumeric():
        return int(s)
    else:
        for i in range(len(s)):
            if s[i].isnumeric():
                answer+=str(s[i])

            elif s[i-3] =='z' and s[i-2] =='e' and s[i-1] =='r' and s[i] == 'o':
                answer +=str(0)
            elif s[i-2] =='o' and s[i-1] =='n' and s[i] == 'e':
                answer +=str(1)
            elif s[i-2] =='t' and s[i-1] =='w' and s[i] == 'o':
                answer +=str(2)
            elif s[i-4] =='t' and s[i-3] =='h' and s[i-2] =='r' and s[i-1] =='e' and s[i] == 'e':
                answer +=str(3)
            elif s[i-3] =='f' and s[i-2] =='o' and s[i-1] =='u' and s[i] == 'r':
                answer +=str(4)
            elif s[i-3] =='f' and s[i-2] =='i' and s[i-1] =='v' and s[i] == 'e':
                answer +=str(5)
            elif s[i-2] =='s' and s[i-1] =='i' and s[i] == 'x':
                answer +=str(6)
            elif s[i-4] =='s' and s[i-3] =='e' and s[i-2] =='v' and s[i-1] =='e' and s[i] == 'n':
                answer +=str(7)
            elif s[i-4] =='e' and s[i-3] =='i' and s[i-2] =='g' and s[i-1] =='h' and s[i] == 't':
                answer +=str(8)
            elif s[i-3] =='n' and s[i-2] =='i' and s[i-1] =='n' and s[i] == 'e':
                answer +=str(9)
        return int(answer)