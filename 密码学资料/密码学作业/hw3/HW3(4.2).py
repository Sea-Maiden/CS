def feistel_round(block, sub_key):
    assert len(block) % 2 == 0, "Block size must be even."
    half_block_size = len(block) // 2
    left, right = block[:half_block_size], block[half_block_size:]

    # 确保sub_key的长度与block的一半长度相同
    if len(sub_key) != half_block_size:
        raise ValueError("Sub-key must match the size of half the block.")
    
    # 创建新的右半部分
    new_right = ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(right, sub_key))
    # 结果是前一个right和新的right的结合
    return left + new_right

def encrypt(plaintext, keys):
    assert len(keys) == len(plaintext) // 2, "There must be a sub-key for each half block."
    block = plaintext
    for key in keys:
        block = feistel_round(block, key)
    return block

def decrypt(ciphertext, keys):
    assert len(keys) == len(ciphertext) // 2, "There must be a sub-key for each half block."
    block = ciphertext
    for key in reversed(keys):
        block = feistel_round(block, key)
    return block

# 创建足够长的密钥，以便每个feistel_round都能用到一个单独的密钥
keys = ['k1', 'k2', 'k3', 'k4']

plaintext = "hellotherehello"  # 确保这个长度是偶数，这样它可以被平分
ciphertext = encrypt(plaintext, keys)
print(f'Encrypted: {ciphertext}')

decrypted = decrypt(ciphertext, keys)
print(f'Decrypted: {decrypted}')

assert plaintext == decrypted
