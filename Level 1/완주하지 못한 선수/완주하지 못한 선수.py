# def solution(participant, completion):
#     answer = ''
#     tmp = completion
#     for i in range(len(participant)):
#         if participant[i] in completion:
#             tmp.pop(completion.index(participant[i])) 
#             continue
#         elif participant[i] not in tmp:
#             answer = participant[i]
#     return answer

def solution(participant, completion):
    participant.sort()
    completion.sort()
    for p,c in zip(participant, completion):
        if p != c:
            return p
    return participant.pop()