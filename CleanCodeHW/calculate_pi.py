import random

# Constants
RADIUS = 1
NUM_POINTS = 1_000_000  # Total number of points to generate
AREA_MULTIPLIER = 4  # Factor to scale the circle area
SQUARE_EXPONENT = 2  # Exponent for squaring values

points_inside_circle = 0

# Monte Carlo method to estimate Pi
for _ in range(NUM_POINTS):
    x_coordinate = random.uniform(-RADIUS, RADIUS)
    y_coordinate = random.uniform(-RADIUS, RADIUS)
    if x_coordinate**SQUARE_EXPONENT + y_coordinate**SQUARE_EXPONENT <= RADIUS**SQUARE_EXPONENT:
        points_inside_circle += 1

# Compute Pi approximation
estimated_pi = (points_inside_circle / NUM_POINTS) * AREA_MULTIPLIER

print(f"Estimated value of Pi: {estimated_pi}")