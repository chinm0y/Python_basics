import numpy as np
import matplotlib.pyplot as plt

def plot_matrix(matrix):
    plt.imshow(matrix, cmap='viridis', interpolation='nearest')
    plt.colorbar()
    plt.title('Matrix Visualization')
    plt.xlabel('Columns')
    plt.ylabel('Rows')
    plt.xticks(ticks=np.arange(matrix.shape[1]), labels=np.arange(1, matrix.shape[1] + 1))
    plt.yticks(ticks=np.arange(matrix.shape[0]), labels=np.arange(1, matrix.shape[0] + 1))
    for (i, j), val in np.ndenumerate(matrix):
        plt.text(j, i, f'{val}', ha='center', va='center', color='white')
    plt.show()