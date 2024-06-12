import math

def shanks_algorithm(alpha, beta, p):
    # Step 1: Initialize
    m = math.ceil(math.sqrt(p))
    
    # Step 2: Baby-step
    baby_steps = {}
    for i in range(m):
        value = pow(alpha, i, p)
        baby_steps[value] = i
    
    # Step 3: Giant-step
    inv_alpha_m = pow(alpha, -m, p)
    giant_step = beta
    for j in range(m):
        if giant_step in baby_steps:
            i = baby_steps[giant_step]
            return j * m + i
        giant_step = (giant_step * inv_alpha_m) % p
    
    return None

# Test cases from the problem
alpha1, beta1, p1 = 106, 12375, 24691
alpha2, beta2, p2 = 6, 248388, 458009

log1 = shanks_algorithm(alpha1, beta1, p1)
log2 = shanks_algorithm(alpha2, beta2, p2)

print(log1, log2)
