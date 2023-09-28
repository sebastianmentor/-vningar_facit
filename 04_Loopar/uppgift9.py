_3X3 = [[1,2,3],
        [4,5,6],
        [7,8,9]]

_4X4 = [[1 ,2 ,3 ,4 ],
        [5 ,6 ,7 ,8 ],
        [9 ,10,11,12],
        [13,14,15,16]]

def rotate_matrix_90(matrix) -> None:
    N =  len(matrix)

    for i in range(N//2):

        for j in range(i, N-i-1):
            
            matrix[i][j],matrix[j][-i-1] = matrix[j][-i-1],matrix[i][j]

            matrix[-j-1][i], matrix[i][j] = matrix[i][j], matrix[-j-1][i]

            matrix[-j-1][i], matrix[-i -1][-j -1] =  matrix[-i -1][-j -1],matrix[-j-1][i]

print(10*'-')
for row in _3X3:
    print(row)

print(10*'-')
rotate_matrix_90(_3X3)
for row in _3X3:
    print(row)

print(10*'-')
rotate_matrix_90(_3X3)
for row in _3X3:
    print(row)

print(10*'-')
rotate_matrix_90(_3X3)
for row in _3X3:
    print(row)

print(10*'-')
rotate_matrix_90(_3X3)
for row in _3X3:
    print(row)

