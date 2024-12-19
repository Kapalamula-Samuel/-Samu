import numpy as np

# Manual calculation of matrix multiplication
def manual_matrix_multiplication(A, B):
    # Initialize the result matrix with zeros
    result = np.zeros((A.shape[0], B.shape[1]))
    # Iterate through rows of A
    for i in range(A.shape[0]):
        # Iterate through columns of B
        for j in range(B.shape[1]):
            # Calculate the dot product for the element at position (i, j)
            for k in range(A.shape[1]):
                result[i][j] += A[i][k] * B[k][j]
    return result

# Using NumPy functions for matrix multiplication
def numpy_matrix_multiplication(A, B):
    # Utilize NumPy's dot function for efficient multiplication
    return np.dot(A, B)

# Scratch implementation of matrix multiplication
def scratch_matrix_multiplication(A, B):
    # Validate that the matrices can be multiplied
    if A.shape[1] != B.shape[0]:
        raise ValueError("Incompatible dimensions for matrix multiplication.")
    # Initialize the result matrix with zeros
    result = np.zeros((A.shape[0], B.shape[1]))
    # Iterate through rows of A
    for i in range(A.shape[0]):
        # Iterate through columns of B
        for j in range(B.shape[1]):
            # Calculate the dot product for the element at position (i, j)
            result[i][j] = sum(A[i][k] * B[k][j] for k in range(A.shape[1]))
    return result

# Handling input validation
def validate_matrices(A, B):
    # Check if the matrices can be multiplied
    if A.shape[1] != B.shape[0]:
        raise ValueError("Incompatible dimensions for matrix multiplication.")

# Matrix transposition
def transpose_matrix(matrix):
    # Return the transposed version of the matrix
    return np.transpose(matrix)

# Example usage
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Manual multiplication
manual_result = manual_matrix_multiplication(A, B)
print("Manual Result:\n", manual_result)

# NumPy multiplication
numpy_result = numpy_matrix_multiplication(A, B)
print("NumPy Result:\n", numpy_result)

# Scratch multiplication
scratch_result = scratch_matrix_multiplication(A, B)
print("Scratch Result:\n", scratch_result)

# Transpose example
transposed_A = transpose_matrix(A)
print("Transposed A:\n", transposed_A)
