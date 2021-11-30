# def solution(s):
#     s = list(s)
#     i = 0

#     while True:
#         if s[i-1] == '(' and s[i] == ')':
#             del s[i-1:i+1]
#             if i>3:
#                 i = i-3
#             else:
#                 i = 0
#         elif len(s)-1 > i:
#             i+=1

#         if len(s) == 0:
#             return True
#         elif len(s)-1 == i:
#             return False

def solution(s):
    stack = []

    for i in s:
        if i =="(":
            stack.append(i)

        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()

    return len(stack)==0