def solution(d, budget):
    d = sorted(d)
    answer = 0
    cost = 0
    for i in range(len(d)):
        cost +=d[i]
        if budget>=cost:
            answer+=1
        else:
            break

    return answer