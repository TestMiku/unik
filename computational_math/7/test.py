import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import subprocess
from io import BytesIO

# Define the function
f = np.exp

# Define interval and number of intervals
a, b = 0, 2
N = 5  # Number of intervals, which gives us N+1 points
h = (b - a) / N  # Step size

# Define points and values of the function at these points
x_points = np.linspace(a, b, N + 1)
f_values = f(x_points)

# Second-order spline coefficients calculation
coeffs = []

for i in range(len(x_points) - 1):
    x_i, x_next = x_points[i], x_points[i + 1]
    f_i, f_next = f_values[i], f_values[i + 1]
    
    # Calculate coefficients for the quadratic spline
    a_i = f_i
    b_i = (f_next - f_i) / h  # Using h directly
    c_i = (f_next - f_i - b_i * h) / (h ** 2)  # Using h in the quadratic term
    
    coeffs.append((a_i, b_i, c_i))

# Test points to evaluate the spline
x_test = np.linspace(a, b, 50)
f_test = f(x_test)

# Calculate spline values s(x) and delta at test points
s_values = []
deltas = []

for x in x_test:
    # Find the corresponding interval for each x in x_test
    for i in range(len(x_points) - 1):
        if x_points[i] <= x <= x_points[i + 1]:
            a_i, b_i, c_i = coeffs[i]
            x_i = x_points[i]
            s_x = a_i + b_i * (x - x_i) + c_i * (x - x_i) ** 2
            s_values.append(s_x)
            deltas.append(abs(f(x) - s_x))
            break

# Create table with results
results_df = pd.DataFrame({
    "x": x_test,
    "f(x)": f_test,
    "s(x)": s_values,
    "delta": deltas
})
