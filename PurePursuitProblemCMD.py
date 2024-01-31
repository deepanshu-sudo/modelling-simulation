import math

def simulate_ppp(xb, yb, xf, yf, vf, minutes):
    for i in range(minutes):
        distance = math.sqrt((math.pow(xb[i] - xf, 2) + math.pow(yb[i] - yf, 2)))

        if distance < 10:
            print("Shot in 4K @ x-coordinate ", xb[i], ", y-coordinate ", yb[i], " at ", i + 1, " th minute, after distance: ", distance)
            break
        else:
            sine = (yb[i] - yf) / distance
            cosine = (xb[i] - xf) / distance

            xf += vf * cosine
            yf += vf * sine

        print("direction @ x: ", xf, ", y: ", yf, " at ", i + 1, "th minute, after d: ", distance)

x_positions_bomber = [80, 90, 99, 108, 116, 125, 133, 141, 151, 160, 169, 179, 180]
y_positions_bomber = [0, -2, -5, -9, -15, -18, -23, -29, -28, -25, -21, -20, -17]
x_initial_fighter = 0
y_initial_fighter = 50
velocity_fighter = 20
minutes = 12

simulate_ppp(x_positions_bomber, y_positions_bomber, x_initial_fighter, y_initial_fighter, velocity_fighter, minutes)
