def solution(numbers):
    answer = []
    for i in range(len(numbers)-1):
        for j in range(len(numbers)):
            if i !=j:
                answer.append(numbers[i]+numbers[j])
    return sorted(set(answer))