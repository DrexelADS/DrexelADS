import threading

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

threads = []
num_threads = 2
chunk_size = size // num_threads
for i in range(num_threads):
    thread = threading.Thread(
        target=calculate_new_rows,
        args=(large_matrix, new_matrix, i * chunk_size, (i + 1) * chunk_size),
    )
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
