import random

class FiniteGroup:
    def __init__(self, order):
        self._order = order
        self._generator = random.randint(2, order - 1)
    
    def order(self):
        return self._order
    
    def generator(self):
        return self._generator
    
    def random_element(self):
        return random.randint(2, self._order - 1)

class OracleDDH:
    def __init__(self, G):
        self.G = G
        
    def is_DDH_tuple(self, g, g_a, g_b, g_ab):
        # Simulated DDH oracle logic for this example
        a = pow(g_a, 1, self.G.order())
        b = pow(g_b, 1, self.G.order())
        return pow(g, a * b, self.G.order()) == g_ab

class ElGamal:
    def __init__(self, G, alpha, beta):
        self.G = G
        self.alpha = alpha
        self.beta = beta
    
    def encrypt(self, x):
        k = random.randint(1, self.G.order() - 1)
        y1 = pow(self.alpha, k, self.G.order())
        y2 = (x * pow(self.beta, k, self.G.order())) % self.G.order()
        return (y1, y2)

class OracleDISTINGUISH:
    def __init__(self, G):
        self.G = G
    
    def distinguish(self, x1, x2, y1, y2):
        # Simulated distinguishing logic for this example
        return y2 in [(x1 * y1) % self.G.order(), (x2 * y1) % self.G.order()]

def distinguish_ElGamal_encryptions(x1, x2, y1, y2, oracle_ddh):
    g = oracle_ddh.G.generator()
    beta = oracle_ddh.G.random_element()
    
    is_DDH_1 = oracle_ddh.is_DDH_tuple(g, y1, beta, y2 * pow(x1, -1, oracle_ddh.G.order()))
    is_DDH_2 = oracle_ddh.is_DDH_tuple(g, y1, beta, y2 * pow(x2, -1, oracle_ddh.G.order()))
    
    if is_DDH_1:
        return True
    elif is_DDH_2:
        return True
    else:
        return False

def solve_DDH(g, g_a, g_b, g_ab, oracle_distinguish):
    x1 = 1
    x2 = 2
    y1 = g_a
    y2_1 = g_ab
    y2_2 = (g_ab * pow(g_a, -1, oracle_distinguish.G.order())) % oracle_distinguish.G.order()
    
    if oracle_distinguish.distinguish(x1, x2, y1, y2_1):
        return True
    elif oracle_distinguish.distinguish(x1, x2, y1, y2_2):
        return False
    else:
        return False

# Example usage
order = 1019  # A prime number for the order of the group
G = FiniteGroup(order)
alpha = G.generator()
beta = G.random_element()
oracle_ddh = OracleDDH(G)
elgamal = ElGamal(G, alpha, beta)

x1 = random.randint(1, order - 1)
x2 = random.randint(1, order - 1)
y1, y2 = elgamal.encrypt(x1)

result_distinguish = distinguish_ElGamal_encryptions(x1, x2, y1, y2, oracle_ddh)
print(f"ElGamal encryption distinguishing result: {result_distinguish}")

oracle_distinguish = OracleDISTINGUISH(G)

g = G.generator()
a = random.randint(1, order - 1)
b = random.randint(1, order - 1)
g_a = pow(g, a, G.order())
g_b = pow(g, b, G.order())
g_ab = pow(g, a * b, G.order())

result_solve_ddh = solve_DDH(g, g_a, g_b, g_ab, oracle_distinguish)
print(f"Decision Diffie-Hellman result: {result_solve_ddh}")

