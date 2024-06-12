import random
from sympy import mod_inverse

# Simulated Oracle-DISTINGUISH function
def oracle_distinguish(x1, x2, y1, y2, p):
    # Simulate the oracle by checking if (y1^(-1) * y2) % p equals x1 or x2
    y1_inv = mod_inverse(y1, p)
    if (y1_inv * y2 % p == x1) or (y1_inv * y2 % p == x2):
        return True
    return False

def solve_ddh(g, g_a, g_b, g_c, p, oracle_distinguish):
    """
    Solves the DDH problem using Oracle-DISTINGUISH.
    
    Args:
    g: Generator of the group.
    g_a: g^a mod p for some secret a.
    g_b: g^b mod p for some secret b.
    g_c: g^c mod p for some secret c.
    p: Prime modulus.
    oracle_distinguish: Function simulating the Oracle-DISTINGUISH.
    
    Returns:
    True if (g, g_a, g_b, g_c) is a valid Diffie-Hellman tuple (i.e., c = ab mod (p-1)).
    False otherwise.
    """
    
    # Choose two random plaintexts x1 and x2 from the group
    x1 = random.randint(1, p-1)  # Example: simple integers as group elements
    x2 = random.randint(1, p-1)  # Example: simple integers as group elements
    
    # Create ciphertexts using g_a and g_b
    y1_x1 = g_a  # g^a mod p
    y2_x1 = (x1 * g_c) % p  # x1 * g^c mod p
    
    y1_x2 = g_b  # g^b mod p
    y2_x2 = (x2 * g_c) % p  # x2 * g^c mod p
    
    # Check if (y1_x1, y2_x1) is a valid encryption of either x1 or x2
    if oracle_distinguish(x1, x2, y1_x1, y2_x1, p):
        return True
    
    # Check if (y1_x2, y2_x2) is a valid encryption of either x1 or x2
    if oracle_distinguish(x1, x2, y1_x2, y2_x2, p):
        return True
    
    return False

# Example usage
# Define simple group elements and generator
p = 104729  # Example large prime
g = 5  # Example generator
a = random.randint(1, p-1)
b = random.randint(1, p-1)
c = (a * b) % (p-1)  # For a valid DDH tuple

g_a = pow(g, a, p)  # g^a mod p
g_b = pow(g, b, p)  # g^b mod p
g_c = pow(g, c, p)  # g^c mod p

# Use the solve_ddh function with the simulated oracle_distinguish
is_ddh_tuple = solve_ddh(g, g_a, g_b, g_c, p, oracle_distinguish)
print(is_ddh_tuple)
