# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

# Hint: The basic equation of a circle is x2 + y2 = r2.


# The Monte Carlo method is a statistical technique that uses random sampling to solve problems. 
# In this case, we can use it to estimate the value of π.

# The steps to solve this problem are as follows:

# Drawing a square with side length 2r (where r is the radius of the circle) and center at the origin.
# Drawing a circle with radius r and center at the origin.
# Randomly generating points within the square.
# Count the number of points that fall within the circle.
# Calculate the ratio of the number of points within the circle to the total number of points generated.
# Multiply this ratio by 4 to get an estimate of π.
# The reason why we multiply the ratio by 4 is because the area of the circle is πr^2, 
# and the area of the square is (2r)^2 = 4r^2. 
# Therefore, the ratio of the area of the circle to the area of the square is π/4.


# import random
# def estimate_pi(n):
#     r = 1.0
#     num_points_circle = 0
#     num_points_total = 0

#     for _ in range(n):
#         x = random.uniform(-r, r)
#         y = random.uniform(-r, r)

#         if x**2 + y**2 <= r**2:
#             num_points_circle += 1

#         num_points_total += 1
    
#     return 4.0 * num_points_circle / num_points_total


import random
import matplotlib.pyplot as plt

def estimate_pi(n):
    r = 1.0
    num_points_circle = 0
    num_points_total = 0
    x_in_circle = []
    y_in_circle = []
    x_out_circle = []
    y_out_circle = []

    for _ in range(n):
        x = random.uniform(-r, r)
        y = random.uniform(-r, r)
        if x**2 + y**2 <= r**2:
            num_points_circle += 1
            x_in_circle.append(x)
            y_in_circle.append(y)
        else:
            x_out_circle.append(x)
            y_out_circle.append(y)
        num_points_total += 1

    pi_estimate = 4.0 * num_points_circle / num_points_total
    return pi_estimate, x_in_circle, y_in_circle, x_out_circle, y_out_circle


pi, x_in, y_in, x_out, y_out = estimate_pi(1000000)


fig, ax = plt.subplots()
circle = plt.Circle((0,0), radius=1.0, color='black', fill=False)
ax.add_artist(circle)
ax.set_xlim(-1.1, 1.1)
ax.set_ylim(-1.1, 1.1)
ax.set_aspect('equal')
ax.scatter(x_in, y_in, color='pink')
ax.scatter(x_out, y_out, color='purple')
plt.title(f"π estimate: {pi:.5f}")
plt.show()

