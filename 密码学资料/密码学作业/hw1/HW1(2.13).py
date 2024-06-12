from sympy import Matrix

def letter_to_index(letter):
    return ord(letter) - ord('A')

def index_to_letter(index):
    return chr(index + ord('A'))

def find_hill_encryption_matrix(plaintext, ciphertext):
    # Ensure the plaintext and ciphertext are the same length
    if len(plaintext) != len(ciphertext):
        raise ValueError("Plaintext and ciphertext must be the same length.")
    
    # Convert plaintext and ciphertext into number arrays
    plaintext_numbers = [letter_to_index(char) for char in plaintext.upper()]
    ciphertext_numbers = [letter_to_index(char) for char in ciphertext.upper()]

    # Determine the size of the matrix we can form (we start from 2 and go up)
    for size in range(2, len(plaintext_numbers) // 2 + 1):
        if len(plaintext_numbers) % size == 0:
            # Split the plaintext and ciphertext into chunks of the determined size
            plaintext_matrix = []
            ciphertext_matrix = []
            for i in range(0, len(plaintext_numbers), size):
                plaintext_matrix.append(plaintext_numbers[i:i+size])
                ciphertext_matrix.append(ciphertext_numbers[i:i+size])
            
            # Create Matrix objects for plaintext and ciphertext
            P = Matrix(plaintext_matrix).T  # .T to transpose for correct matrix orientation
            C = Matrix(ciphertext_matrix).T
            
            # Attempt to compute the inverse of the plaintext matrix
            try:
                P_inv = P.inv_mod(26)
            except ValueError:
                # If the matrix is not invertible modulo 26, try the next size
                continue
            
            # Compute the key matrix K
            K = C * P_inv % 26
            
            # Return the key matrix if successful
            return K, size
    
    # If no invertible matrix found, return None
    return None, None

# Example plaintext and ciphertext from the exercise
plaintext_example = "breathtaking"
ciphertext_example = "RUPOTENTOIFV"

# Find the encryption matrix
encryption_matrix, matrix_size = find_hill_encryption_matrix(plaintext_example, ciphertext_example)

# Output the result
if encryption_matrix:
    print(f"Encryption matrix of size {matrix_size}x{matrix_size}:")
    print(encryption_matrix)
else:
    print("No suitable encryption matrix found.")
