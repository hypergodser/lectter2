import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

# Create a figure and an axis
fig, ax = plt.subplots()

# Set plot limits so the line stays nicely in view
ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(-1.1, 1.1)

# Generate initial data
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

# Create a line object that will be updated during the animation
(line,) = ax.plot(x, y)


# Function to update the plot for each frame
def update(frame):
  # Shift the sine wave
  line.set_ydata(np.sin(x + frame / 10.0))
  return (line,)


# Create an animation object
ani = animation.FuncAnimation(
    fig, update, frames=100, interval=50, blit=True
)

# Display the animation
plt.show()