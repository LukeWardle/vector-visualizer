#!/usr/bin/env python3
"""Generate example visualizations for README."""
import os
from src.plot_utils import plot_vector, plot_multiple_vectors
# Create examples directory
os.makedirs('examples', exist_ok=True)
# Example 1: Single vector
print("Generating single vector example...")
plot_vector(
    [3, 4],
    save_path='examples/single_vector.png',
    color='blue'
)
# Example 2: Vector comparison
print("Generating vector comparison...")
plot_multiple_vectors(
    [[3, 4], [5, 12], [-2, 3]],
    labels=['Vector A', 'Vector B', 'Vector C'],
    colors=['blue', 'red', 'green'],
    save_path='examples/vector_comparison.png'
)
# Example 3: Vector addition
print("Generating vector addition...")
a = [3, 2]
b = [1, 4]
c = [a[0] + b[0], a[1] + b[1]]
plot_multiple_vectors(
    [a, b, c],
    labels=['a', 'b', 'a + b'],
    colors=['blue', 'green', 'red'],
    save_path='examples/vector_addition.png'
)
# Example 4: Force decomposition
print("Generating force decomposition...")
import numpy as np
# 45-degree force decomposed into x and y components
magnitude = 5
angle = np.pi / 4  # 45 degrees
force = [magnitude * np.cos(angle), magnitude * np.sin(angle)]
x_component = [force[0], 0]
y_component = [0, force[1]]
plot_multiple_vectors(
    [force, x_component, y_component],
    labels=['Force', 'X Component', 'Y Component'],
    colors=['red', 'blue', 'green'],
    save_path='examples/force_decomposition.png'
)
print("\n✓ All examples generated in examples/ directory")
