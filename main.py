def adjacency_list_to_matrix(adj_list):
    # Determine the number of nodes
    if not adj_list:
        return []

    n = max(adj_list.keys()) + 1  # assuming nodes are labeled from 0 to max_node
    # Initialize the adjacency matrix with zeros
    matrix = [[0] * n for _ in range(n)]

    # Populate the matrix based on adjacency list
    for node, neighbors in adj_list.items():
        for neighbor in neighbors:
            matrix[node][neighbor] = 1

    # Print each row of the adjacency matrix
    for row in matrix:
        print(row)

    return matrix
