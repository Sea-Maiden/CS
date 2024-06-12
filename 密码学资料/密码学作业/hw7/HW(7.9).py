import sympy

# 定义参数
p = 31847
alpha = 5
a = 7899

# 定义一个函数进行解密
def elgamal_decrypt(c1, c2, p, a):
    s = pow(c1, a, p)
    s_inv = sympy.mod_inverse(s, p)
    m = (c2 * s_inv) % p
    return m

# 示例密文对
ciphertext_pairs = [(3781, 14409)]

# 解密示例
for c1, c2 in ciphertext_pairs:
    m = elgamal_decrypt(c1, c2, p, a)
    print(f"Decrypted number: {m}")

    # 解码为字母
    first_letter = chr((m // (26**2)) + ord('A'))
    second_letter = chr(((m // 26) % 26) + ord('A'))
    third_letter = chr((m % 26) + ord('A'))
    print(f"Decrypted text: {first_letter}{second_letter}{third_letter}")
