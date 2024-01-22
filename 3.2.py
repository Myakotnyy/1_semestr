# Функция для поворота матрицы
def povorot_matrix(mat: list[list[int]]) -> None:

    k = len(mat[0])

# Делаем матрицу квадратной, добавляя нули
    while len(mat) < len(mat[0]): 
        mat.append([0]*len(mat[0]))

    while len(mat) > len(mat[0]):
        for i in range(len(mat)):
            mat[i].append(0)

# Меняем элементы матрицы местами 
    for i in range(len(mat)):
        for n in range(i, len(mat)):
            mat[i][n], mat[n][i] = mat[n][i], mat[i][n]

# Удаляем нули и лишние строки
            if mat[i][n] == 0:
                mat[i].remove(0)

    while len(mat) > k:
        mat.pop()

    return print(mat)


if __name__ == '__main__':
    mat = [[1 , 2 , 3 , 4 ],
           [5 , 6 , 7 , 8 ],
           [9 , 10, 11, 12],
           [13, 14, 15, 16]]
    povorot_matrix(mat)