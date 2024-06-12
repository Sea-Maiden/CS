import numpy as np

# Define the size of the binary tuple
n = 3

# Generate all possible binary tuples for n=3
binary_tuples = np.array([[int(x) for x in format(i, f'0{n}b')] for i in range(2**n)])

# Initialize an empty encryption matrix of size 2^n x 2^n
encryption_matrix = np.zeros((2**n, 2**n), dtype=int)

# Construct the encryption matrix
# Each entry of the encryption matrix is the XOR of the binary tuples representing plaintext and key
encryption_matrix_output = ""  # Initialize an empty string to capture the output
for i, plaintext in enumerate(binary_tuples):
    for j, key in enumerate(binary_tuples):
        encryption_matrix[i, j] = int(''.join(str((p ^ k)) for p, k in zip(plaintext, key)), 2)
    # Add the matrix row to the output string
    encryption_matrix_output += " ".join(str(num) for num in encryption_matrix[i, :]) + "\n"

# Print the encryption matrix in the desired output format
print(encryption_matrix_output)
encryption_matrix  # This will also show the matrix as an array output
