def create_matrix():
    # Создаем двумерный массив размером 3x3 и заполняем его числами от 1 до 9
    matrix = [[0] * 3 for _ in range(3)]
    count = 1

    for i in range(3):
        for j in range(3):
            matrix[i][j] = count
            count += 1

    return matrix


def print_matrix_rows(matrix):
    # Выводим строку из элементов каждой строки массива
    for row in matrix:
        row_string = " ".join(map(str, row))
        print(row_string)


def main():
    # Создаем двумерный массив
    matrix = create_matrix()

    # Выводим строку из элементов каждой строки массива
    print_matrix_rows(matrix)


if __name__ == "__main__":
    main()