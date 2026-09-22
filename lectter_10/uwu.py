import numpy as np

random_matrix = np.random.randint(1, 11, size=(3, 3))
print(random_matrix,random_matrix.shape)  # Output: A 3x3 matrix with random integers between 1 and 10

matrix_sum = np.sum(random_matrix)
print(matrix_sum)  # Output: Sum of all elements in the random_matrix

matrix_mean = np.mean(random_matrix)
print(matrix_mean)  # Output: Mean of all elements in the random_matrix

transposed_matrix = np.transpose(random_matrix)
print(transposed_matrix)  # Output: Transposed version of the random_matrix