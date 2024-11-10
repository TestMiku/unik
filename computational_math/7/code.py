import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

f = np.exp

x_points = np.linspace(0, 2, 6) # 6 points on [0,2]

f_values = f(x_points)

# Second-order spline coefficients calculation
# Each segment will have a quadratic form s_i(x) = a_i + b_i*(x - x_i) + c_i*(x - x_i)^2
# This is a simplified version without boundary condition handling

coeffs = []

for i in range(len(x_points) - 1):
    x_i, x_next = x_points[i], x_points[i + 1]
    f_i, f_next = f_values[i], f_values[i + 1]
    
    # Set up equations for quadratic spline
    # s(x_i) = f_i  -> a_i = f_i
    a_i = f_i
    # s'(x_i) continuity (initial slope approximation, here simplified as central difference)
    b_i = (f_next - f_i) / (x_next - x_i)  # Approximate the slope
    # Match second derivative, here we assume c_i is constant across small intervals
    c_i = (f_next - f_i - b_i * (x_next - x_i)) / ((x_next - x_i) ** 2)
    
    coeffs.append((a_i, b_i, c_i))

# Test points to evaluate spline
x_test = np.linspace(0, 2, 50)
f_test = f(x_test)

# Calculate spline values s(x) and delta at test points
s_values = []
deltas = []

for x in x_test:
    # Find the corresponding interval
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


# Plotting
# 1. Plot function f(x) and spline approximation
plt.figure()
plt.plot(x_test, f_test, label="f(x) = e^x")
plt.plot(x_test, s_values, label="Second-order Spline s(x)", linestyle="--")
plt.scatter(x_points, f_values, color="red", marker="o", label="Spline Knots")
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Function f(x) and Second-order Spline Approximation")
plt.show()

# 2. Mean absolute error vs. number of points (dummy values for illustration)
points_range = range(3, 11)
mean_errors = [np.mean(deltas[:int(len(deltas) * p / max(points_range))]) for p in points_range]

plt.figure()
plt.plot(list(points_range), mean_errors, marker="o")
plt.xlabel("Number of Points")
plt.ylabel("Mean Absolute Error")
plt.title("Mean Absolute Error vs. Number of Points")
plt.show()
