import numpy as np

# Probabilities for plaintexts
prob_P = {'a': 1/2, 'b': 1/3, 'c': 1/6}

# Since all keys are equally likely, their probabilities are 1/3 each.
prob_K = 1/3

# Entropy of the plaintext
H_P = -sum(prob * np.log2(prob) for prob in prob_P.values())

# Entropy of the key (since all keys are equiprobable, we use the formula for entropy of a uniform distribution)
H_K = -3 * (prob_K * np.log2(prob_K))

# Output the entropies
print(H_P, H_K)

# Given encryption matrix as a dictionary for easy manipulation
encryption_matrix = {
    'K1': {'a': 1, 'b': 2, 'c': 3},
    'K2': {'a': 2, 'b': 3, 'c': 4},
    'K3': {'a': 3, 'b': 4, 'c': 1}
}

# Calculate the probability distribution for C
prob_C = {1: 0, 2: 0, 3: 0, 4: 0}

for plaintext, p in prob_P.items():
    for key, encrypted_values in encryption_matrix.items():
        prob_C[encrypted_values[plaintext]] += p * prob_K

# Entropy of the ciphertext
H_C = -sum(prob * np.log2(prob) for prob in prob_C.values())

# Now calculate the conditional entropy H(K|C)
# This requires the joint probability distribution of K and C, which we can derive from encryption_matrix

# Initialize the joint probability dictionary
joint_prob_KC = {k: {1: 0, 2: 0, 3: 0, 4: 0} for k in encryption_matrix}

# Calculate the joint probability for every K and C
for key, mappings in encryption_matrix.items():
    for plaintext, encrypted_value in mappings.items():
        joint_prob_KC[key][encrypted_value] += prob_P[plaintext] * prob_K

# Calculate the marginal probability for C
marginal_prob_C = {c: sum(joint_prob_KC[key][c] for key in joint_prob_KC) for c in prob_C}

# Calculate the conditional entropy H(K|C)
H_K_given_C = 0
for key in joint_prob_KC:
    for c in joint_prob_KC[key]:
        if joint_prob_KC[key][c] > 0:
            H_K_given_C -= joint_prob_KC[key][c] * np.log2(joint_prob_KC[key][c] / marginal_prob_C[c])

# Output the entropies
print(H_C, H_K_given_C)
