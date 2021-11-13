def solution(sizes):
    for i in range(len(sizes)):
        sizes[i] = sorted(sizes[i])

    answer = 1
    row = []
    col = []

    for i in range(len(sizes)):
        row.append(sizes[i][0])
        col.append(sizes[i][1])
    answer = max(row)*max(col)
    return answer