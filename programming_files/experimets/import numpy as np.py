import numpy as np
import matplotlib.pyplot as plt
import meshpy.triangle as triangle

def generate_structured_mesh(num_points_x, num_points_y):
    # Create a grid of points
    x = np.linspace(0, 1, num_points_x)
    y = np.linspace(0, 1, num_points_y)
    X, Y = np.meshgrid(x, y)

    # Triangulate the points
    points = np.vstack([X.ravel(), Y.ravel()]).T
    A = np.array([(i, i + num_points_x + 1, i + 1) for i in range((num_points_y - 1) * num_points_x) if (i + 1) % num_points_x != 0])
    B = np.array([(i + 1, i + num_points_x + 1, i + num_points_x) for i in range((num_points_y - 1) * num_points_x) if (i + 1) % num_points_x != 0])
    triangles = np.vstack([A, B])

    return points, triangles

def generate_unstructured_mesh(points):
    def round_trip_connect(start, end):
        return [(i, i + 1) for i in range(start, end)] + [(end, start)]

    # Define the points and the boundary facets
    info = triangle.MeshInfo()
    info.set_points(points)
    info.set_facets(round_trip_connect(0, len(points) - 1))

    # Generate the mesh
    mesh = triangle.build(info, max_volume=0.01, min_angle=25)
    return np.array(mesh.points), np.array(mesh.elements)

# Structured mesh generation
num_points_x, num_points_y = 10, 10
points_structured, triangles_structured = generate_structured_mesh(num_points_x, num_points_y)

# Plot structured mesh
plt.figure(figsize=(12, 6))
plt.subplot(121)
plt.triplot(points_structured[:, 0], points_structured[:, 1], triangles_structured, color='black')
plt.title('Structured Triangular Mesh')
plt.gca().set_aspect('equal')

# Unstructured mesh generation
points = np.random.rand(30, 2)
points_unstructured, triangles_unstructured = generate_unstructured_mesh(points)

# Plot unstructured mesh
plt.subplot(122)
plt.triplot(points_unstructured[:, 0], points_unstructured[:, 1], triangles_unstructured, color='black')
plt.title('Unstructured Triangular Mesh')
plt.gca().set_aspect('equal')

plt.show()
