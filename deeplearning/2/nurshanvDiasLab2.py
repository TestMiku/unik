import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import toeplitz
from scipy.linalg import solve

L = 1.0       
T = 0.2       
Nx = 50       
Nt = 1000     
alpha = 0.01  

dx = L / (Nx - 1)
dt = T / Nt

CFL = alpha * dt / dx**2
if CFL > 0.5:
    raise ValueError(f"dt is to large! The CFL stability condition is violated: {CFL:.2f}")

# coords
x = np.linspace(0, L, Nx)
t = np.linspace(0, T, Nt)

# The initial condition: f(x) = sin(pi*x)
U = np.zeros((Nx, Nt))
U[:, 0] = np.sin(np.pi * x)

# Boundary conditions (Dirichlet): U(first) = 0, U(last) = 0
U[0, :] = 0
U[-1, :] = 0

# Forward Problem: Euler Method 
for n in range(0, Nt - 1):
    for i in range(1, Nx - 1):
        U[i, n + 1] = U[i, n] + CFL * (U[i - 1, n] - 2 * U[i, n] + U[i + 1, n])

# adding noise
noise_level = 0.02
U_noisy = U[:, -1] + noise_level * np.random.randn(Nx)

# Inverse problem: Tichonov regularization. 
A = np.eye(Nx) + CFL * (np.diag(np.ones(Nx-1), -1) - 2*np.eye(Nx) + np.diag(np.ones(Nx-1), 1))

lambda_values = [0.01, 0.1, 1]
plt.figure(figsize=(10, 6))
plt.plot(x, U[:, 0], label="True initial condition f(x)", color='black', linewidth=2)

for lam in lambda_values:
    I = np.eye(Nx)
    A_reg = np.dot(A.T, A) + lam * I
    U_reg = solve(A_reg, np.dot(A.T, U_noisy))

    plt.plot(x, U_reg, label=f"Recovered f(x) (λ={lam})", linestyle="--")

plt.xlabel("x")
plt.ylabel("Temperature")
plt.legend()
plt.title("Comparison of true and recovered initial conditions")
plt.show()
