import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

x_min, x_max=0, 2

N = 100

t, t_max = 0, 1

dx = (x_max-x_min)/(N-1)
dt = 0.02

a = 1
c = a * (dt/dx)

if c==1:
    print('Число Курента подходит')
else:
    print('Число Курента не подходит')

x_coordinates = np.linspace(x_min, x_max, N)
u_current = np.exp(-200 * (x_coordinates-0.2)**2)
u_new = np.zeros(len(u_current))

solution_matrix = [u_current.copy()]
num_time_steps = int(t_max/dt)

for step in range(num_time_steps):
    for i in range(1, N-1):
        u_new[i] = u_current[i] - c*(u_current[i] - u_current[i-1])

    u_new[0] = u_current[0] - c * (u_current[0] - u_current[-2])
    u_new[-1] = u_current[0]
    u_current[:] = u_new
    solution_matrix.append(u_new.copy())


print(f"u({50}) = {max(solution_matrix[50])}")

is_animate = True 
is_animate = False 
if is_animate:
    fig, axis_x = plt.subplots()
    line, = axis_x.plot(x_coordinates, solution_matrix[0], color='red')
    axis_x.set_xlim(x_min, x_max)
    axis_x.set_ylim(0, t_max)
    axis_x.set_xlabel('x')
    axis_x.set_xlabel('u(x,t)')
    axis_x.set_label("perenos equations")
    def update_plot(frame, x_coordinates, y, line):
        line.set_ydata(y[frame])
        return line,
    ani = animation.FuncAnimation(fig, update_plot, frames=range(len(solution_matrix)), 
                                  fargs=(x_coordinates, solution_matrix, line), interval=50, blit=True)
    plt.show()
else:
    fig, axis_x = plt.subplots()
    line, = axis_x.plot(x_coordinates, solution_matrix[50], color='red')
    axis_x.set_xlim(x_min, x_max)
    axis_x.set_ylim(0, t_max)
    axis_x.set_xlabel('x')
    axis_x.set_xlabel('u(x,t)')

    axis_x.set_label("perenos equations")

    plt.show()
