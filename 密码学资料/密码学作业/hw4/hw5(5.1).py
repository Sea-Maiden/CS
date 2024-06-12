import numpy as np

A = np.array([
    [1, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 1, 1, 0, 0],
    [0, 0, 1, 1, 1, 1, 0],
    [0, 0, 0, 1, 1, 1, 1]
])

b = np.array([0, 1, 0, 1])

def solve_mod2(A, b):
    A = np.hstack([A, b.reshape(-1, 1)])  
    rows, cols = A.shape
    
    for r in range(rows):
       
        pivot = None
        for c in range(r, cols - 1):
            if A[r, c] == 1:
                pivot = c
                break
                
        if pivot is None:
            continue
        
        if A[r, pivot] == 0:
            for rr in range(r + 1, rows):
                if A[rr, pivot] == 1:
                    A[[r, rr]] = A[[rr, r]]
                    break
        
        for rr in range(rows):
            if rr != r and A[rr, pivot] == 1:
                A[rr] = (A[rr] + A[r]) % 2
    
    x = np.zeros(cols - 1, dtype=int)
    for r in range(rows):
        non_zero_col = np.nonzero(A[r, :-1])[0]
        if len(non_zero_col) == 1:
            x[non_zero_col[0]] = A[r, -1]
    
    return x

x = solve_mod2(A, b)
print(x)
