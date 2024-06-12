# 定义一个函数，使用给定的密钥使用移位密码解密密文
def decrypt_shift_cipher(ciphertext, key):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha(): # 检查字符是否为字母表
            shift = (ord(char) - key - 65) % 26 + 65 # 按键值向后移
            decrypted_text += chr(shift)
        else:
            decrypted_text += char
    return decrypted_text

# 给定暗文
ciphertexts = ['APNDJI', 'XYGROBO']

# 因为我们不知道shift/key的值，所以我们尝试从1到25的所有可能性
# 对于一个有效的移位密码，密钥永远不会是0，因为那意味着没有加密，也不会是26，因为它是一个完整的循环。
for ciphertext in ciphertexts:
    print(f"Trying decryption for {ciphertext}:")
    for key in range(1, 26):
        decrypted = decrypt_shift_cipher(ciphertext, key)
        print(f"Key {key}: {decrypted}")
    print("\n")  