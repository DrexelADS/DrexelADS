# Adjacency List

# A-B
# |
# C

graph_list = {
    "A": ["B", "C"],
    "B": [],
    "C": ["B"]
}

graph_list_ud = {
    "A": ["B", "C"],
    "B": ["A"],
    "C": ["A"],
}

graph_mat = [
    # A   B   C
    [ 0,  1,  1 ],  # A
    [ 0,  0,  0 ],  # B
    [ 0,  1,  0 ],  # C
]

graph_mat_ud = [
    # A   B   C
    [ 0,  1,  1 ],  # A
    [ 1,  0,  0 ],  # B
    [ 1,  0,  0 ],  # C
]
