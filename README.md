```markdown
# Adjacency List to Matrix Converter

This Python project provides a function to convert an adjacency list representation of a graph into an adjacency matrix. It supports both directed and undirected graphs and handles graphs with non-sequential node labels.

## Description

An adjacency list is a dictionary where each key is a node, and its value is a list of nodes that the key node is connected to. The adjacency matrix is a 2D list (matrix) where each element at position `[i][j]` is 1 if there is an edge from node `i` to node `j`, and 0 otherwise.

## Usage

Define the function `adjacency_list_to_matrix(adj_list)` in your Python script or interactive environment, then pass your adjacency list as an argument.

### Example

```python
# Example adjacency list
adj_list = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [2]
}

# Convert to adjacency matrix
matrix = adjacency_list_to_matrix(adj_list)
# Output:
# [0, 1, 1, 0]
# [0, 0, 1, 0]
# [1, 0, 0, 1]
# [0, 0, 1, 0]
``

### Function Definition

``
python
def adjacency_list_to_matrix(adj_list):
    if not adj_list:
        return []

    n = max(adj_list.keys()) + 1
    matrix = [[0] * n for _ in range(n)]

    for node, neighbors in adj_list.items():
        for neighbor in neighbors:
            matrix[node][neighbor] = 1

    for row in matrix:
        print(row)

    return matrix
``

## Features

- Handles graphs with non-sequential node labels
- Supports directed graphs
- Prints the adjacency matrix row by row
- Returns the adjacency matrix as a list of lists

## License

This project is open source and free to use.
