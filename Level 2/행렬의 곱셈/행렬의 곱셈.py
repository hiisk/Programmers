def solution(arr1, arr2):
    answer = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]
    for x in range(len(arr1)):
        for i in range(len(arr2[0])):
            for j in range(len(arr1[0])):
                answer[x][i] += arr1[x][j]* arr2[j][i]
    return answer