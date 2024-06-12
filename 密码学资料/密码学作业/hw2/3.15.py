import numpy as np
# Given plaintext probabilities
prob_a = 1/2
prob_b = 1/3
prob_c = 1/6

# Since each key is equally likely, the probability of each key is 1/3.
prob_key = 1/3

# Calculate the probability of each ciphertext outcome (1, 2, 3, 4)
# For each ciphertext, sum the probabilities of the plaintext/key pairs that produce it
prob_ciphertexts = {
    1: prob_a * prob_key + prob_c * prob_key,  # From a with K1 and c with K3
    2: prob_a * prob_key + prob_b * prob_key,  # From a with K2 and b with K1
    3: prob_a * prob_key + prob_b * prob_key + prob_c * prob_key,  # From a with K3, b with K2, c with K1
    4: prob_b * prob_key + prob_c * prob_key   # From b with K3 and c with K2
}

# Entropy of the ciphertext H(C)
H_C = -sum(prob * np.log2(prob) for prob in prob_ciphertexts.values())

print(H_C)
