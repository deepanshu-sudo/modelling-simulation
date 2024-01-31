import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Function to simulate and animate the pursuit
def animate(i, xb, yb, xf, yf, vf, caught, ax, info_text):
    # Clear previous frame
    ax.clear()

    # Set plot limits
    ax.set_xlim(0, 200)
    ax.set_ylim(-50, 100)

    # Plot bomber and fighter positions
    if caught and i >= caught_index:
        ax.plot(xf[caught_index], yf[caught_index], 'rx', label='Caught Here', markersize=10)
        ax.annotate(info_text, (xf[caught_index], yf[caught_index]),
                    textcoords="offset points", xytext=(10,-10), ha='center')
        ax.plot(xf[:i+1], yf[:i+1], 'yo--', label='Fighter Path', alpha=0.1)
        ax.plot(xb[:i+1], yb[:i+1], 'ko--', label='Bomber Path', alpha=0.1)
    else:
        ax.plot(xf[:i+1], yf[:i+1], 'bo--', label='Fighter Path')
        ax.plot(xb[:i+1], yb[:i+1], 'ro--', label='Bomber Path')

    # Add legend and labels
    ax.legend()
    ax.set_title("Pure Pursuit Problem")
    ax.set_xlabel("X Coordinate")
    ax.set_ylabel("Y Coordinate")

# Define the simulation logic
def simulate_ppp(xb, yb, xf, yf, vf, minutes):
    x_fighter, y_fighter = [xf], [yf]
    caught = False
    caught_index = -1
    info_text = ""
    
    for i in range(minutes):
        distance = math.sqrt((math.pow(xb[i] - xf, 2) + math.pow(yb[i] - yf, 2)))

        if distance < 10 and not caught:
            caught = True
            caught_index = i
            info_text = f"Caught at minute {i + 1}: ({xb[i]}, {yb[i]})"
            print(info_text)
        else:
            sine = (yb[i] - yf) / distance
            cosine = (xb[i] - xf) / distance

            xf += vf * cosine
            yf += vf * sine

        x_fighter.append(xf)
        y_fighter.append(yf)

    return x_fighter, y_fighter, caught, caught_index, info_text

# Initial positions and velocity
x_positions_bomber = [80, 90, 99, 108, 116, 125, 133, 141, 151, 160, 169, 179, 180]
y_positions_bomber = [0, -2, -5, -9, -15, -18, -23, -29, -28, -25, -21, -20, -17]
x_initial_fighter = 0
y_initial_fighter = 50
velocity_fighter = 20
minutes = 12

# Simulate the pursuit to get the fighter path
x_fighter, y_fighter, caught, caught_index, info_text = simulate_ppp(x_positions_bomber, y_positions_bomber, x_initial_fighter, y_initial_fighter, velocity_fighter, minutes)

# Create a figure and axis
fig, ax = plt.subplots()

# Create the animation
ani = FuncAnimation(fig, animate, frames=len(x_fighter), fargs=(x_positions_bomber, y_positions_bomber, x_fighter, y_fighter, velocity_fighter, caught, ax, info_text), interval=1000, repeat=False)

# Show the animation
plt.show()