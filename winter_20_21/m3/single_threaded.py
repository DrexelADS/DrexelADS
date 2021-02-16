size = 2000

large_matrix = [list(range(size)) for _ in range(size)]


def add_power_tuple_row_to_mat(mat, row, mat_ind):
    new_row = []
    for num in row:
        new_row.append((num, num ** 2, num ** 3))

    mat[mat_ind] = new_row


def calculate_new_rows(mat, new_mat, start, num_rows):
    for i in range(start, num_rows):
        add_power_tuple_row_to_mat(new_mat, mat[i], i)


new_matrix = [None for _ in range(size)]

calculate_new_rows(large_matrix, new_matrix, 0, size)
