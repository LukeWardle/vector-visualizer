"""Test script for multiple vector plotting."""
from src.plot_utils import plot_multiple_vectors
# Example 1: Basic comparison
print("Test 1: Comparing two vectors...")
plot_multiple_vectors(
    [[3, 4], [5, 12]],
    save_path='outputs/comparison_basic.png'
)
# Example 2: Labeled vectors with custom colors
print("Test 2: Forces comparison...")
plot_multiple_vectors(
    [[4, 3], [-2, 5], [1, -3]],
    labels=['Force A', 'Force B', 'Force C'],
    colors=['blue', 'red', 'green'],
    save_path='outputs/comparison_forces.png'
)
# Example 3: Vector addition visualization
print("Test 3: Vector addition...")
a = [3, 2]
b = [1, 4]
c = [a[0] + b[0], a[1] + b[1]]  # Sum vector
plot_multiple_vectors(
    [a, b, c],
    labels=['a', 'b', 'a + b'],
    colors=['blue', 'green', 'red'],
    save_path='outputs/vector_addition.png'
)
print("\n✓ All tests completed! Check outputs/ directory.")
