def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        new_row = []
        for col in row:
            new_row.append(col ** 2)
        new_matrix.append(new_row)
    return new_matrix

if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    new_matrix = square_matrix_simple(matrix)
    print(new_matrix)
    print(matrix)