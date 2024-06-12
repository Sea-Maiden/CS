from sympy import Matrix, mod_inverse

# 将字母转换为数字
def letters_to_numbers(letters):
    return [ord(letter) - ord('A') for letter in letters.upper()]

# 将文本转换为数字，假设它已经是大写且没有空格或非字母字符
def text_to_numeric(text):
    return [letters_to_numbers(text[i:i+3]) for i in range(0, len(text), 3)]

# 使用明文和密文求解加密矩阵
def solve_hill_cipher(plaintext, ciphertext):
    # 将明文和密文分割成大小为3的块，并转换为数字
    plaintext_blocks = text_to_numeric(plaintext)
    ciphertext_blocks = text_to_numeric(ciphertext)

    # 使用第一个块来确定加密矩阵
    P = Matrix(plaintext_blocks[0:3])
    C = Matrix(ciphertext_blocks[0:3])

    # 求加密矩阵A，使P * A = C mod 26
    # P求模26的倒数解A
    try:
        P_inv = P.inv_mod(26)
    except ValueError as e:
        return str(e), None  # If the inverse doesn't exist, return the error message

    A = P_inv * C % 26
    return None, A

# 给定明文和密文
plaintext = "breathtaking"
ciphertext = "RUPOTENTOIFV"

# 假设n = 3，求解加密矩阵
error, encryption_matrix = solve_hill_cipher(plaintext, ciphertext)

# 检查矩阵是否找到并打印出来
if encryption_matrix:
    # Format and print the matrix
    matrix_as_list = encryption_matrix.tolist()
    formatted_matrix = '\n'.join(['\t'.join(map(str, row)) for row in matrix_as_list])
    print("Encryption matrix:\n", formatted_matrix)
else:
    # If there was an error, print it
    print("Error:", error)