import numpy as np

def gauss_inverse(A):
    A = np.array(A, dtype=float)
    n = len(A)
    identity = np.eye(n)
    augmented = np.hstack((A, identity))  # create extended matrix (A | I)
    
    # forward step
    for i in range(n):
        augmented[i] /= augmented[i, i]
        for j in range(n):
            if i != j:
                augmented[j] -= augmented[i] * augmented[j, i]
    
    return augmented[:, n:]  # return right part of matrix (A^(-1))

def tikhonov_regularization(A, b, lam):
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    
    n = A.shape[1]
    I = np.eye(n)
    regularized_matrix = A.T @ A + lam * I  # (A^T A + λI)
    inverse_regularized = gauss_inverse(regularized_matrix)
    
    return inverse_regularized @ (A.T @ b)  # (A^T A + λI)^(-1) A^T b

A = np.array([[1, 2], [2, 4.001]])
b = np.array([3, 6.001])

# without regularization (forward)
inverse_A = gauss_inverse(A)
x_direct = inverse_A @ b
print(f"Solution without regulization: {x_direct}")

lambda_values = [0, 1, 10, 100]
for lam in lambda_values:
    x_reg = tikhonov_regularization(A, b, lam)
    print(f"Solution with regulization(λ={lam}): {x_reg}")

# Analysis
# When λ=0, the Tikhonov method coincides with the ordinary solution.
# As λ increases, regularization smooths out instability but may bias the solution.
# For large values of λ, the solution significantly differs from the direct method.
    """
    $ python deeplearning/1/nurshanovDiasLab1.py 
    Solution without regulization: [1. 1.]
    Solution with regulization(λ=0): [1.00000002 0.99999997]
    Solution with regulization(λ=1): [0.57682251 1.15387572]
    Solution with regulization(λ=10): [0.42853061 0.85723264]
    Solution with regulization(λ=100): [0.12000832 0.24006464]
    """