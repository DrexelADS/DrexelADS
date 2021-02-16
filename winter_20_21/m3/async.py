import asyncio

size = 2000

large_matrix = [list(range(size)) for _ in range(size)]


async def add_power_tuple_row_to_mat(mat, row, mat_ind):
    new_row = []
    for num in row:
        new_row.append((num, num ** 2, num ** 3))

    mat[mat_ind] = new_row


async def calculate_new_rows(mat, new_mat, start, num_rows):
    promises = []
    for i in range(start, num_rows):
        promise = add_power_tuple_row_to_mat(new_mat, mat[i], i)
        promises.append(promise)
    await asyncio.gather(*promises)


async def make_new_matrix():
    new_matrix = [None for _ in range(size)]
    num_divisions = 8
    promises = []
    for i in range(num_divisions):
        chunk_size = size // num_divisions
        promise = calculate_new_rows(
            large_matrix, new_matrix, i * chunk_size, (i + 1) * chunk_size
        )
        promises.append(promise)
    await asyncio.gather(*promises)


loop = asyncio.get_event_loop()
loop.run_until_complete(make_new_matrix())
loop.close()
