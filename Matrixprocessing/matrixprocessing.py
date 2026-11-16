def read_matrix():
    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    return n, m, matrix


def main():
    n_a, m_a, matrix_a = read_matrix()
    n_b, m_b, matrix_b = read_matrix()

    if n_a != n_b or m_a != m_b:
        print("ERROR")
        return

    for i in range(n_a):
        row = [str(matrix_a[i][j] + matrix_b[i][j]) for j in range(m_a)]
        print(" ".join(row))


if __name__ == "__main__":
    main()

def read_matrix():
    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    return n, m, matrix


def main():
    n, m, matrix = read_matrix()
    constant = int(input())

    for i in range(n):
        row = [str(matrix[i][j] * constant) for j in range(m)]
        print(" ".join(row))


if __name__ == "__main__":
    main()

def parse_number(token):
    if "." in token:
        return float(token)
    return int(token)


def format_number(num):
    if isinstance(num, float) and num.is_integer():
        return str(int(num))
    return str(round(num, 6)) if isinstance(num, float) else str(num)


def read_matrix(size_prompt, matrix_prompt):
    n, m = map(int, input(size_prompt).split())
    print(matrix_prompt)
    matrix = [[parse_number(x) for x in input().split()] for _ in range(n)]
    return n, m, matrix


def print_matrix(matrix):
    print("The result is:")
    for row in matrix:
        print(" ".join(format_number(x) for x in row))


def add_matrices():
    n_a, m_a, matrix_a = read_matrix("Enter size of first matrix: ", "Enter first matrix:")
    n_b, m_b, matrix_b = read_matrix("Enter size of second matrix: ", "Enter second matrix:")

    if n_a != n_b or m_a != m_b:
        print("The operation cannot be performed.")
        return

    result = [
        [matrix_a[i][j] + matrix_b[i][j] for j in range(m_a)]
        for i in range(n_a)
    ]
    print_matrix(result)


def multiply_by_constant():
    n, m, matrix = read_matrix("Enter size of matrix: ", "Enter matrix:")
    constant = parse_number(input("Enter constant: "))

    result = [
        [matrix[i][j] * constant for j in range(m)]
        for i in range(n)
    ]
    print_matrix(result)


def multiply_matrices():
    n_a, m_a, matrix_a = read_matrix("Enter size of first matrix: ", "Enter first matrix:")
    n_b, m_b, matrix_b = read_matrix("Enter size of second matrix: ", "Enter second matrix:")

    if m_a != n_b:
        print("The operation cannot be performed.")
        return

    result = [
        [
            sum(matrix_a[i][k] * matrix_b[k][j] for k in range(m_a))
            for j in range(m_b)
        ]
        for i in range(n_a)
    ]
    print_matrix(result)


def main():
    while True:
        print("1. Add matrices")
        print("2. Multiply matrix by a constant")
        print("3. Multiply matrices")
        print("0. Exit")
        choice = input("Your choice: ")

        if choice == "1":
            add_matrices()
        elif choice == "2":
            multiply_by_constant()
        elif choice == "3":
            multiply_matrices()
        elif choice == "0":
            break
        print()


if __name__ == "__main__":
    main()

def parse_number(token):
    if "." in token:
        return float(token)
    return int(token)


def format_number(num):
    if isinstance(num, float) and num.is_integer():
        return str(int(num))
    return str(round(num, 6)) if isinstance(num, float) else str(num)


def read_matrix(size_prompt, matrix_prompt):
    n, m = map(int, input(size_prompt).split())
    print(matrix_prompt)
    matrix = [[parse_number(x) for x in input().split()] for _ in range(n)]
    return n, m, matrix


def print_matrix(matrix):
    print("The result is:")
    for row in matrix:
        print(" ".join(format_number(x) for x in row))


def add_matrices():
    n_a, m_a, matrix_a = read_matrix("Enter size of first matrix: ", "Enter first matrix:")
    n_b, m_b, matrix_b = read_matrix("Enter size of second matrix: ", "Enter second matrix:")

    if n_a != n_b or m_a != m_b:
        print("The operation cannot be performed.")
        return

    result = [
        [matrix_a[i][j] + matrix_b[i][j] for j in range(m_a)]
        for i in range(n_a)
    ]
    print_matrix(result)


def multiply_by_constant():
    n, m, matrix = read_matrix("Enter size of matrix: ", "Enter matrix:")
    constant = parse_number(input("Enter constant: "))

    result = [
        [matrix[i][j] * constant for j in range(m)]
        for i in range(n)
    ]
    print_matrix(result)


def multiply_matrices():
    n_a, m_a, matrix_a = read_matrix("Enter size of first matrix: ", "Enter first matrix:")
    n_b, m_b, matrix_b = read_matrix("Enter size of second matrix: ", "Enter second matrix:")

    if m_a != n_b:
        print("The operation cannot be performed.")
        return

    result = [
        [
            sum(matrix_a[i][k] * matrix_b[k][j] for k in range(m_a))
            for j in range(m_b)
        ]
        for i in range(n_a)
    ]
    print_matrix(result)


def transpose_matrix():
    print("1. Main diagonal")
    print("2. Side diagonal")
    print("3. Vertical line")
    print("4. Horizontal line")
    trans_choice = input("Your choice: ")

    n, m, matrix = read_matrix("Enter matrix size: ", "Enter matrix:")

    if trans_choice == "1":
        result = [[matrix[j][i] for j in range(n)] for i in range(m)]
    elif trans_choice == "2":
        result = [[matrix[n - 1 - j][m - 1 - i] for j in range(n)] for i in range(m)]
    elif trans_choice == "3":
        result = [row[::-1] for row in matrix]
    elif trans_choice == "4":
        result = matrix[::-1]
    else:
        print("The operation cannot be performed.")
        return

    print_matrix(result)


def main():
    while True:
        print("1. Add matrices")
        print("2. Multiply matrix by a constant")
        print("3. Multiply matrices")
        print("4. Transpose matrix")
        print("0. Exit")
        choice = input("Your choice: ")

        if choice == "1":
            add_matrices()
        elif choice == "2":
            multiply_by_constant()
        elif choice == "3":
            multiply_matrices()
        elif choice == "4":
            transpose_matrix()
        elif choice == "0":
            break
        print()


if __name__ == "__main__":
    main()

def parse_number(token):
    if "." in token:
        return float(token)
    return int(token)


def format_number(num):
    if num == 0:
        return "0"
    if isinstance(num, float) and num.is_integer():
        return str(int(num))
    if isinstance(num, float):
        text = f"{num:.2f}".rstrip("0").rstrip(".")
        return "0" if text in ("", "-0") else text
    return str(num)


def read_matrix(size_prompt, matrix_prompt):
    n, m = map(int, input(size_prompt).split())
    print(matrix_prompt)
    matrix = [[parse_number(x) for x in input().split()] for _ in range(n)]
    return n, m, matrix


def print_matrix(matrix):
    print("The result is:")
    for row in matrix:
        print(" ".join(format_number(x) for x in row))


def add_matrices():
    n_a, m_a, matrix_a = read_matrix("Enter size of first matrix: ", "Enter first matrix:")
    n_b, m_b, matrix_b = read_matrix("Enter size of second matrix: ", "Enter second matrix:")

    if n_a != n_b or m_a != m_b:
        print("The operation cannot be performed.")
        return

    result = [
        [matrix_a[i][j] + matrix_b[i][j] for j in range(m_a)]
        for i in range(n_a)
    ]
    print_matrix(result)


def multiply_by_constant():
    n, m, matrix = read_matrix("Enter size of matrix: ", "Enter matrix:")
    constant = parse_number(input("Enter constant: "))

    result = [
        [matrix[i][j] * constant for j in range(m)]
        for i in range(n)
    ]
    print_matrix(result)


def multiply_matrices():
    n_a, m_a, matrix_a = read_matrix("Enter size of first matrix: ", "Enter first matrix:")
    n_b, m_b, matrix_b = read_matrix("Enter size of second matrix: ", "Enter second matrix:")

    if m_a != n_b:
        print("The operation cannot be performed.")
        return

    result = [
        [
            sum(matrix_a[i][k] * matrix_b[k][j] for k in range(m_a))
            for j in range(m_b)
        ]
        for i in range(n_a)
    ]
    print_matrix(result)


def transpose_matrix():
    print("1. Main diagonal")
    print("2. Side diagonal")
    print("3. Vertical line")
    print("4. Horizontal line")
    trans_choice = input("Your choice: ")

    n, m, matrix = read_matrix("Enter matrix size: ", "Enter matrix:")

    if trans_choice == "1":
        result = [[matrix[j][i] for j in range(n)] for i in range(m)]
    elif trans_choice == "2":
        result = [[matrix[n - 1 - j][m - 1 - i] for j in range(n)] for i in range(m)]
    elif trans_choice == "3":
        result = [row[::-1] for row in matrix]
    elif trans_choice == "4":
        result = matrix[::-1]
    else:
        print("The operation cannot be performed.")
        return

    print_matrix(result)


def get_minor(matrix, row, col):
    return [
        [matrix[i][j] for j in range(len(matrix)) if j != col]
        for i in range(len(matrix)) if i != row
    ]


def determinant(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for col in range(n):
        sign = (-1) ** col
        sub_det = determinant(get_minor(matrix, 0, col))
        det += sign * matrix[0][col] * sub_det
    return det


def calculate_determinant():
    n, m, matrix = read_matrix("Enter matrix size: ", "Enter matrix:")
    if n != m:
        print("The operation cannot be performed.")
        return

    det = determinant(matrix)
    print("The result is:")
    print(format_number(det))


def inverse_matrix():
    n, m, matrix = read_matrix("Enter matrix size: ", "Enter matrix:")
    if n != m:
        print("The operation cannot be performed.")
        return

    det = determinant(matrix)
    if det == 0:
        print("This matrix doesn't have an inverse.")
        return

    if n == 1:
        result = [[1 / matrix[0][0]]]
    else:
        cofactors = []
        for i in range(n):
            cofactor_row = []
            for j in range(n):
                sign = (-1) ** (i + j)
                minor_det = determinant(get_minor(matrix, i, j))
                cofactor_row.append(sign * minor_det)
            cofactors.append(cofactor_row)

        adjugate = [[cofactors[j][i] for j in range(n)] for i in range(n)]
        result = [
            [adjugate[i][j] / det for j in range(n)]
            for i in range(n)
        ]

    print_matrix(result)


def main():
    while True:
        print("1. Add matrices")
        print("2. Multiply matrix by a constant")
        print("3. Multiply matrices")
        print("4. Transpose matrix")
        print("5. Calculate a determinant")
        print("6. Inverse matrix")
        print("0. Exit")
        choice = input("Your choice: ")

        if choice == "1":
            add_matrices()
        elif choice == "2":
            multiply_by_constant()
        elif choice == "3":
            multiply_matrices()
        elif choice == "4":
            transpose_matrix()
        elif choice == "5":
            calculate_determinant()
        elif choice == "6":
            inverse_matrix()
        elif choice == "0":
            break
        print()


if __name__ == "__main__":
    main()

