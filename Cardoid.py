import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

def plot_points(ax, num_points):
    for i in range(num_points):
        angle = 2 * np.pi * i / num_points
        x = np.cos(angle)
        y = np.sin(angle)

        ax.plot(x, y, 'o', markersize=4)
        ax.text(x * 1.1, y * 1.1, str(i + 1), ha='center', va='center', fontsize=4, color='white')


def plot_lines(ax, num_points):
    for i in range(num_points):
        angle = 2 * np.pi * i / num_points
        x = np.cos(angle)
        y = np.sin(angle)

        double_index = (i * 2) % num_points
        double_angle = 2 * np.pi * double_index / num_points
        double_x = np.cos(double_angle)
        double_y = np.sin(double_angle)

        ax.plot([x, double_x], [y, double_y], '-', alpha=0.8)
        plt.pause(0.3)


def plot_circle(num_points):
    fig, ax = plt.subplots(facecolor='black')
    
    circle = Circle((0, 0), 1, facecolor='black', edgecolor='white')
    ax.add_artist(circle)
    plt.gca().set_aspect('equal')
    ax.axis('off')

    plot_points(ax, num_points)
    plot_lines(ax, num_points)

    plt.show()


plot_circle(72)
