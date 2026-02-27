"""
Plotting utilities for vector visualization.

This module provides functions to create clear, professional visualizations 
of 2D vectors using matplotlib.

"""
import matplotlib.pyplot as plt
import numpy as np
from typing import List, Tuple, Optional
import os

def plot_vector(
    vector: List[float],
    save_path: str = "outputs/vector_plot.png",
    color: str = "blue",
    show_magnitude:  bool = True
) -> None:
  """
  Plot a 2D vector as an arrow from the origin.

  Creates a professional visualization showing the vector as an arrow,
  with optional magnitude annotation. Saves to file at specified path.

  Args:
    vector: 2D vector as [x, y] list of floats.
    save_path: Output file path for the plot.
    color: Arrow color (matplotlib color name or hex).
    show_magnitude: Whether to display magnitude annotation.

  Raises:
    ValueError: If vector is not 2D.

  Examples:
    >>>plot_vector([3, 4])
    >>>plot_vector([5, 12], color='red', show_magnitude=False) 
  
  """
  # Validate input
  if len(vector) != 2:
    raise ValueError(
      f"Vector must be 2D. Got {len(vector)} dimensions."
    )
  
  # Ensure output directory exists
  os.makedirs(os.path.dirname(save_path), exist_ok=True)

  # Extract components
  x, y = vector[0], vector[1]

  # Calculate magnitude for later use
  magnitude = np.sqrt(x**2 + y**2)

  # Create figure and axis
  fig, ax = plt.subplots(figsize=(8, 8))

  # Draw vector as arrow from origin (0, 0) to (x, y)
  ax.quiver(
    0, 0,                             # Starting point(origin)
    x, y,                             # Vector components
    angles = 'xy',                    # Use cartesian angle interpretation
    scale_units = 'xy',               # Scale in data units
    scale = 1,                        # No scaling (true length)
    color = color,                    # Arrow color
    width = 0.005                     # Arrow shaft width
  )

  # Set axis limits with padding
  # Use max component magnitude plus 20% padding
  max_component = max(abs(x), abs(y))
  limit = max_component * 1.2 if max_component > 0 else 1
  ax.set_xlim(-limit, limit)
  ax.set_ylim(-limit, limit)

  # Add coordinate axes through origin
  ax.axhline(y=0, color='black', linewidth=0.8, alpha=0.7)
  ax.axvline(x=0, color='black', linewidth=0.8, alpha=0.7)

  # Add grid for reference
  ax.grid(True, linestyle='--', alpha=0.4)

  # Set equal aspect ratio so vectors aren't distorted
  ax.set_aspect('equal', adjustable='box')

  # Labels and title
  ax.set_xlabel('X', fontsize=12, fontweight='bold')
  ax.set_ylabel('Y', fontsize=12, fontweight='bold')

  # Create title with vector and magnitude
  title = f'Vector [{x}, {y}]'
  if show_magnitude:
    title += f'\nMagnitude: {magnitude:.3f}'
  ax.set_title(title, fontsize=14, fontweight='bold', pad=20)

  # Add magnitude annotation on the arrow
  if show_magnitude and magnitude > 0:
    # Place text at midpoint of vector
    mid_x, mid_y = x * 0.5, y * 0.5
    ax.text(
      mid_x, mid_y,
      f'||v|| = {magnitude:.3f}',
      fontsize=11,
      color='red',
      bbox=dict(boxstyle='round, pad=0.5', facecolor='white', edgecolor='red', alpha=0.8)
    )

  # Mark the endpoint
  ax.plot(x, y, 'ro', markersize=8, label=f'Endpoint ({x}, {y})')
  ax.plot(0, 0, 'ko', markersize=8, label='Origin (0, 0)')
    
  # Add legend
  ax.legend(loc='upper right', fontsize=10)
    
  # Save with high quality
  plt.tight_layout()
  plt.savefig(save_path, dpi=300, bbox_inches='tight')
  plt.close(fig)  # Free memory
