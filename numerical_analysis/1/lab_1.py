import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

x_min=0
x_max=2

N = 100
t_max = 1
dt = 0.02
a = 1

dx = (x_max-x_min)/(N-1)
c = a * (dt/dx)

if c==1:
    print('Число Курента подходит')
else:
    print('Число Курента не подходит')

x = np.linspace(x_min, x_max, N)
u = np.exp(-200 * (x-0.2)**2)
u_1 = np.zeros(len(u))

solution_matrix = [u.copy()]
time_steps = int(t_max/dt)

for n in range(time_steps):
    for i in range(1, N-1):
        u_1[i] = u[i] - c*(u[i] - u[i-1])

    u_1[0] = u[0] - c * (u[0] - u[-2])
    u_1[-1] = u_1[0]
    u[:] = u_1
    solution_matrix.append(u_1.copy())




fig, axis_x = plt.subplots()
line, = axis_x.plot(x, solution_matrix[0], color='red')
axis_x.set_xlim(x_min, x_max)
axis_x.set_ylim(0, t_max)
axis_x.set_xlabel('x')
axis_x.set_xlabel('u(x,t)')

axis_x.set_label("perenos equations")
def update_plot(frame, x, y, line):
    line.set_ydata(y[frame])
    return line,
ani = animation.FuncAnimation(fig, update_plot, frames=range(len(solution_matrix)), 
                              fargs=(x, solution_matrix, line), interval=50, blit=True)

plt.show()
