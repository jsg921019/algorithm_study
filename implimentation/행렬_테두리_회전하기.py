# https://programmers.co.kr/learn/courses/30/lessons/77485?language=python3

def solution(rows, columns, queries):

    l = [[i*columns + j + 1 for j in range(columns)] for i in range(rows)]

    def rotate(i1, j1, i2, j2):

        idx = [(i1-1, j) for j in range(j1-1, j2-1)]
        idx += [(i, j2-1) for i in range(i1-1, i2-1)]
        idx += [(i2-1, j) for j in range(j2-1, j1-1, -1)]
        idx += [(i, j1-1) for i in range(i2-1, i1-1, -1)]
        
        tmp1 = l[idx[0][0]][idx[0][1]]
        min_val = tmp1

        for i, j in idx[1:]:
            tmp2 = l[i][j]
            l[i][j] = tmp1 
            if tmp2 < min_val:
                min_val = tmp2
            tmp1 = tmp2
        l[idx[0][0]][idx[0][1]] = tmp1
        
        return min_val

    answer = []
    for i1, j1, i2, j2 in queries:
        min_val = rotate(i1, j1, i2, j2)
        answer.append(min_val)
    
    return answer