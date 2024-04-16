import numpy as np
import matplotlib.pyplot as plt
from noise import pnoise2

def radial_fade(height, width):
    """Generate a radial gradient that fades from center to the edges."""
    center_x, center_y = width // 2, height // 2
    radius = min(center_x, center_y)
    y, x = np.ogrid[-center_y:height-center_y, -center_x:width-center_x]
    fade = np.sqrt(x*x + y*y) / radius
    fade = np.clip(1 - fade, 0, 1)  # Clip to avoid negative values
    return fade

def generate_fuzzy_field(width, height, scale=0.1, octaves=5, persistence=0.5, lacunarity=2.0):
    """Generates a fuzzy field using Perlin noise with a radial fade."""
    field = np.zeros((height, width))
    fade = radial_fade(height, width)  # Create the radial fade

    for i in range(height):
        for j in range(width):
            noise_value = pnoise2(i * scale, j * scale,
                                  octaves=octaves,
                                  persistence=persistence,
                                  lacunarity=lacunarity)
            field[i][j] = noise_value * fade[i][j]  # Apply the radial fade

    return field

# Parameters
width, height = 100, 100
scale = 0.1  # Determines the zoom level of the noise

# Generate fuzzy field
fuzzy_field = generate_fuzzy_field(width, height, scale)

# Plotting the field
plt.figure(figsize=(8, 6))
plt.imshow(fuzzy_field, cmap='gray')
plt.colorbar()
plt.title("Fuzzy Field with Radial Fade")
plt.show()
