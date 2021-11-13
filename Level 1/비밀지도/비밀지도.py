def solution(n, arr1, arr2):
    answer = []
    for x, y in zip(arr1,arr2):
        temp = str(bin(x|y)[2:])
        temp = temp.rjust(n,'0')
        temp = temp.replace('1','#')
        temp = temp.replace('0',' ')
        answer.append(temp)
    return answer