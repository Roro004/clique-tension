import numpy as np
import matplotlib.pyplot as plt

def radial_gradient(height, width):
    """Generate a radial gradient that is black in the center and fades to white towards the edges."""
    center_x, center_y = width // 2, height // 2
    y, x = np.ogrid[-center_y:height-center_y, -center_x:width-center_x]
    # Calculate distance to the center
    distance = np.sqrt(x**2 + y**2)
    max_dist = np.sqrt(center_x**2 + center_y**2)
    gradient = distance / max_dist
    # Ensure the center is fully black and smoothly transitions to white
    gradient = gradient ** 0.5  # Adjust the exponent for more control over the fade
    return gradient

# Parameters
width, height = 300, 300

# Generate radial gradient
fuzzy_circle = radial_gradient(height, width)

# Plotting the gradient
plt.figure(figsize=(8, 6))
plt.imshow(fuzzy_circle, cmap='gray', interpolation='bilinear')
plt.colorbar()
plt.title("Fuzzy Circle Gradient")
plt.axis('off')  # Hide the axis
plt.show()
