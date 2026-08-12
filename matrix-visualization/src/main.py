
from matrix_utils import create_matrix, calculate_term
from plot_utils import plot_matrix

def main():
    # Create a matrix
    matrix = create_matrix(5, 5)  # Example: 5x5 matrix

    # Calculate a specific term of the matrix
    term = calculate_term(matrix, 2, 3)  # Example: calculate term at position (2, 3)

    print(f"Matrix:\n{matrix}")
    print(f"Term at (2, 3): {term}")

    # Visualize the matrix
    plot_matrix(matrix)

if __name__ == "__main__":
    main()