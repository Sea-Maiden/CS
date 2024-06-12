def decrypt(ciphertext, K, pi):
    # 反置换字典
    pi_inverse = {v: k for k, v in pi.items()}
    
    # 解密函数
    def dz(y, z):
        return pi_inverse[(y - z) % 26]

    plaintext = ''
    for i, c in enumerate(ciphertext):
        z = (K + i) % 26
        y = ord(c) - ord('A')
        x = dz(y, z)
        plaintext += chr(x + ord('A'))
    
    return plaintext

# 置换π
pi = {0: 23, 1: 13, 2: 24, 3: 0, 4: 7, 5: 15, 6: 14, 7: 6, 8: 25, 9: 16, 10: 22, 11: 1, 12: 19, 
      13: 18, 14: 5, 15: 11, 16: 17, 17: 2, 18: 21, 19: 12, 20: 20, 21: 4, 22: 10, 23: 9, 24: 3, 25: 8}

ciphertext = "WRTCNRLDSAFARWKXFTXCZRNHNYPDTZUUKMPLUSOXNEUDOKLXRMCBKGRCCURR"

# 尝试每个可能的密钥K
for K in range(26):
    plaintext = decrypt(ciphertext, K, pi)
    print(f"K={K}: {plaintext}")
