import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams.update({'font.size': 14})  # Use larger font for plots.

r = 3.89  # Parameter
x0 = 0.5  # Starting population
N = 100  # Number of time steps
x = [x0]  # List to store iterations

for i in range(1, N+1):
    x.append(r*x[i-1]*(1 - x[i-1]))

y0 = 0.49
y = [y0]
for i in range(1, N+1):
    y.append(r*y[i-1]*(1 - y[i-1]))

plt.plot(range(N+1), x, label="$x_0$=0.50")
plt.plot(range(N+1), y, label="$x_0$=0.49")

plt.xlabel(r"Time step $n$")
plt.ylabel(r"$x_n$")
plt.title("Logistic map with $r$={:.2f}".format(r, x0))
plt.xlim([0, N])
plt.ylim([0, 1])
lgd = plt.legend(bbox_to_anchor=[1,0.9,0.2,0.1])

# plt.show()  # Uncomment to show interactive plot.

# Uncomment to save high-resolution figure to disk.
plt.savefig("logistic_map_plot.png", dpi=150, transparent=True, bbox_extra_artists=(lgd,), bbox_inches='tight') 
