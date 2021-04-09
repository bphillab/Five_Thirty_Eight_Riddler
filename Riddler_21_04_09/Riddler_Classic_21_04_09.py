import numpy as np


def grid_number_to_array(num):
    return [(num // 2 ** _) % 2 for _ in range(12)]


def translate_arr_to_dict(arr):
    conn = {}
    if arr[0] == 0:
        conn[0] = conn.get(0, []) + [1]
    else:
        conn[1] = conn.get(1, []) + [0]
    if arr[1] == 0:
        conn[1] = conn.get(1, []) + [2]
    else:
        conn[2] = conn.get(2, []) + [1]
    if arr[2] == 0:
        conn[0] = conn.get(0, []) + [3]
    else:
        conn[3] = conn.get(3, []) + [0]
    if arr[3] == 0:
        conn[1] = conn.get(1, []) + [4]
    else:
        conn[4] = conn.get(4, []) + [1]
    if arr[4] == 0:
        conn[2] = conn.get(2, []) + [5]
    else:
        conn[5] = conn.get(5, []) + [2]
    if arr[5] == 0:
        conn[3] = conn.get(3, []) + [4]
    else:
        conn[4] = conn.get(4, []) + [3]
    if arr[6] == 0:
        conn[4] = conn.get(4, []) + [5]
    else:
        conn[5] = conn.get(5, []) + [4]
    if arr[7] == 0:
        conn[3] = conn.get(3, []) + [6]
    else:
        conn[6] = conn.get(6, []) + [3]
    if arr[8] == 0:
        conn[4] = conn.get(4, []) + [7]
    else:
        conn[7] = conn.get(7, []) + [4]
    if arr[9] == 0:
        conn[5] = conn.get(5, []) + [8]
    else:
        conn[5] = conn.get(5, []) + [8]
    if arr[10] == 0:
        conn[6] = conn.get(6, []) + [7]
    else:
        conn[7] = conn.get(7, []) + [6]
    if arr[11] == 0:
        conn[7] = conn.get(7, []) + [8]
    else:
        conn[8] = conn.get(8, []) + [7]
    return conn


def is_solvable(num):
    connections = translate_arr_to_dict(grid_number_to_array(num))
    old = []
    visited = connections.get(0, [])
    while old != visited and 8 not in visited:
        old = visited
        visited = np.unique(visited + sum([connections.get(_, []) for _ in visited], [])).tolist()
    return 8 in visited


if __name__ == "__main__":
    counter = 0
    cases = 0
    for i in range(2 ** 12):
        cases = cases + 1
        counter = counter + is_solvable(i)
    print("Percent solvable: ", counter / cases)
