# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

# Hint: The basic equation of a circle is x2 + y2 = r2.


import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# Set up the plot
fig, ax = plt.subplots()
ax.set_xlim([-1.1, 1.1])
ax.set_ylim([-1.1, 1.1])
plt.gca().set_aspect('equal', adjustable='box')
plt.xticks([])
plt.yticks([])

ax.set_title("Estimating Pi with Monte Carlo Method")

# Draw the circle with origin at center and radius 1
circle = plt.Circle((0, 0), 1, fill=False, edgecolor='black')
ax.add_artist(circle)

# the number of points to use
n_points = 1000

# Initialize counts and lists to store points
inside_count = 0
outside_count = 0
x_inside, y_inside = [], []
x_outside, y_outside = [], []

# Animate function
def animate(i):
    global inside_count, outside_count, x_inside, y_inside, x_outside, y_outside

    for i in range(n_points):
        # Generate random points
        x = np.random.uniform(-1, 1)
        y = np.random.uniform(-1, 1)

        # Compute the distance from each point to the origin
        r = np.sqrt(x**2 + y**2)
    
        # Check if the point is inside the circle
        if  r <= 1.0:
            inside_count += 1
            x_inside.append(x)
            y_inside.append(y)
        else:
            outside_count += 1
            x_outside.append(x)
            y_outside.append(y)
    
    # Update scatter plots
    ax.scatter(x_inside, y_inside, color='blue', alpha=0.2)
    ax.scatter(x_outside, y_outside, color='pink', alpha=0.2)
    
    # Calculate and update pi estimation
    pi_estimate = 4 * inside_count / (inside_count + outside_count)
    ax.set_xlabel(f"Inside: {inside_count}, Outside: {outside_count}, Pi Estimate: {pi_estimate:.5f}")
    
    # Write "inside" and "outside" text outside the graph
    ax.annotate("Inside", xy=(0.05, 0.9), xycoords='axes fraction', fontsize=14)
    ax.annotate("Outside", xy=(0.85, 0.9), xycoords='axes fraction', fontsize=14)
    
ani = FuncAnimation(fig, animate, frames=100, interval=100, repeat=False)
plt.show()

