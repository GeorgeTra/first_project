# Напишите функцию для транспонирования матрицы.

from numpy import array, transpose


def transposed_matrix(matrix: list[list[int]]) -> list[list[int]]:
    new_matrix = array(matrix)
    return new_matrix.transpose()


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f'Matrix:\n{array(matrix)}\n')
print(f'Transposed matrix:\n{transposed_matrix(matrix)}')

