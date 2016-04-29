def rowTocol(matrix):
    matrix=zip(*matrix)
    return list(matrix)

mat=[[1,2,3],[4,5,6],[7,8,9]]
print(rowTocol(mat))
