import numpy as np
from fractions import Fraction
from tabulate import tabulate

order_3 = 3

def hilbert_matrix(n):
    H = np.zeros((n, n), dtype=object)  # Use object dtype to store fractions
    for i in range(n):
        for j in range(n):
            H[i, j] = Fraction(1, i + j + 1)  # Create a Fraction object
    return H

def gaussian_elimination(matrix):
    n = len(matrix)
    identity = np.identity(n, dtype=object)  # Use object dtype for the identity matrix
    augmented_matrix = np.hstack((matrix, identity))

    for i in range(n):
        for j in range(i + 1, n):
            factor = augmented_matrix[j, i] / augmented_matrix[i, i]
            augmented_matrix[j, i:] -= factor * augmented_matrix[i, i:]

    for i in range(n - 1, -1, -1):
        augmented_matrix[i, :] /= augmented_matrix[i, i]

        for j in range(i - 1, -1, -1):
            factor = augmented_matrix[j, i]
            augmented_matrix[j, :] -= factor * augmented_matrix[i, :]

    inverse_matrix = augmented_matrix[:, n:]

    return inverse_matrix

def matrix_to_string(matrix):
    n = matrix.shape[0]
    result = np.empty_like(matrix, dtype=object)
    for i in range(n):
        for j in range(n):
            value = matrix[i, j]
            if value == 0:
                result[i, j] = '0'
            elif value == 1:
                result[i,j]='1'
            else:
                result[i, j] = f'{value.numerator}/{value.denominator}'  # Convert to string in "1/2" format
    return result

hilbert_matrix_3 = hilbert_matrix(order_3)
inverse_hilbert_matrix_3 = gaussian_elimination(hilbert_matrix_3)

# Matrix multiplication to get identity
identity_matrix = np.dot(hilbert_matrix_3, inverse_hilbert_matrix_3)

print("Hilbert matrix of order 3")
print(tabulate(matrix_to_string(hilbert_matrix_3), tablefmt="fancy_grid"), "\n")

print("Inverse of Hilbert Matrix of order 3:")
print(tabulate(matrix_to_string(inverse_hilbert_matrix_3), tablefmt="fancy_grid"), "\n")

print("Identity Matrix (Hilbert * Inverse Hilbert):")
print(tabulate(matrix_to_string(identity_matrix), tablefmt="fancy_grid"), "\n")
