def dfs(matrix, row, col, visited):
    # Define the directions for exploring neighbors (up, down, left, right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Mark the current cell as visited
    visited[row][col] = True
    
    # Explore neighbors
    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < len(matrix) and 0 <= new_col < len(matrix[0]) and matrix[new_row][new_col] == 1 and not visited[new_row][new_col]:
            dfs(matrix, new_row, new_col, visited)

def count_shapes(matrix):
    if not matrix:
        return 0
    
    # Initialize visited matrix
    visited = [[False] * len(matrix[0]) for _ in range(len(matrix))]
    
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1 and not visited[i][j]:
                # Perform DFS for each unvisited cell with value 1
                dfs(matrix, i, j, visited)
                count += 1
    
    return count


if __name__ == "__main__":
    # Given matrix
    matrix = [
    [1,1,0,0,0,0,0],
    [1,0,0,0,1,1,0],
    [1,0,0,0,0,1,0],
    [0,0,1,1,0,0,0],
    [0,0,1,0,0,1,1],
    [0,0,1,0,0,1,0]
    ]

# Count unique shapes
num_shapes = count_shapes(matrix)
print("Number of unique shapes:", num_shapes)
