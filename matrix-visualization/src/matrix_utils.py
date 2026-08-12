def create_matrix(rows, cols):
    """Generate a matrix with given rows and columns filled with sequential numbers."""
    return np.arange(1, rows * cols + 1).reshape(rows, cols)

def calculate_term(matrix, row, col):
    """Calculate a specific term of the matrix at the given row and column."""
    if row < 0 or row >= matrix.shape[0] or col < 0 or col >= matrix.shape[1]:
        raise IndexError("Row or column index out of bounds.")
    return matrix[row, col]