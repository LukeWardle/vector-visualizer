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

def plot_multiple_vectors(
    vectors: List[list[float]],
    labels: Optional[List[str]] = None,
    colors: Optional[List[str]] = None,
    save_path: str = 'outputs/vectors_comparison.png',
    show_magnitude: bool = True
) -> None:
  """
  Plot mutliple 2D vectors on the same axes for comparison.

  Creates a visualization showing mutliple vectors as arrows from the origin,
  with the different colors and optional labels for comparison.

  Args:
    vectors: List of 2D vectors, each as [x, y].
    labels: Optional labels for each vector (default to v1, v2, ...).
    colors: Optional colors for each vector (defaults to color palette).
    save_path: Output file path.
    show_magnitude: Whether to display magnitude annotations.

  Raises:
    ValueError: If any vector is not 2D or if vectors list is empty.

  Examples:
    >>>plot_multiple_vectors([[3, 4], [5, 12]])
    >>>plot_mutliple_vectors(
    ...   [[3, 4], [-2, 3]],
    ...   labels=['Force A', 'Force B'],
    ...   colors=['blue', 'red']
    ...   )
  
  """
  # Validate input
  if not vectors:
    raise ValueError("Must provide at least one vector")
  
  for i, vec in enumerate(vectors):
    if len(vec) != 2:
      raise ValueError(
        f"Vector {i} has {len(vec)} dimensions. All must be 2D."
      )
    
  # Ensure output directory exists
  os.makedirs(os.path.dirname(save_path), exist_ok=True)

  # Set default labels if not provided
  if labels is None:
    labels = [f'v{i+1}' for i in range(len(vectors))]

  # Set default colors if not provided
  if colors is None:
    # Professional color palette
    default_colors = ['blue', 'red', 'green', 'orange', 'purple', 'brown']
    colors = [default_colors[i % len(default_colors)] for i in range(len(vectors))]

  # Create figure
  fig, ax = plt.subplots(figsize=(10, 10))

  # Find maximum component for axis scaling
  max_component = 0
  for vec in vectors:
    max_component = max(max_component, abs(vec[0]), abs(vec[1]))

  limit = max_component * 1.3 if max_component > 0 else 1

  # Plot each vector
  for i, (vec, label, color) in enumerate(zip(vectors, labels, colors)):
    x, y = vec[0], vec[1]
    magnitude = np.sqrt(x**2 + y**2)

    # Draw vector arrow
    ax.quiver(
      0, 0, x, y,
      angles='xy', scale_units='xy', scale=1,
      color=color, width=0.005,
      label=f'{label} ||v|| = {magnitude:.3f}'
    )

    # Mark endpoint
    ax.plot(x, y, 'o', color=color, markersize=8)

    # Add magnitude annotation if requested
    if show_magnitude and magnitude > 0:
      # Offset text position slightly to avoid overlap
      offset = 0.1 * i # Stagger annotations
      mid_x, mid_y = x * 0.5 + offset, y * 0.5 + offset
      ax.text(
        mid_x, mid_y,
        f'{magnitude:.2f}',
        fontsize=9,
        color=color,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=color, alpha=0.7)
      )

    
  # Mark origin
  ax.plot(0, 0, 'ko', markersize=10, label='Origin', zorder=5)

  # Configure axes
  ax.set_xlim(-limit, limit)
  ax.set_ylim(-limit, limit)
  ax.axhline(y=0, color='black', linewidth=0.8, alpha=0.7)
  ax.axvline(x=0, color='black', linewidth=0.8, alpha=0.7)
  ax.grid(True, linestyle='--', alpha=0.4)
  ax.set_aspect('equal', adjustable='box')
    
  # Labels and title
  ax.set_xlabel('X', fontsize=12, fontweight='bold')
  ax.set_ylabel('Y', fontsize=12, fontweight='bold')
  ax.set_title(
    f'Vector Comparison ({len(vectors)} vectors)',
    fontsize=14, fontweight='bold', pad=20
  )
    
  # Add legend
  ax.legend(loc='best', fontsize=10, framealpha=0.9)
    
  # Save
  plt.tight_layout()
  plt.savefig(save_path, dpi=300, bbox_inches='tight')
  plt.close(fig)




