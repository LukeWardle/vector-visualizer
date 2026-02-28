#!/usr/bin/env python

"""
Vector Visualizer CLI

Command-line interface for creating vector visualization.

"""

import argparse
import sys
from src.plot_utils import plot_vector

def parse_arguments():
  """Parse command-line arguments."""
  parser = argparse.ArgumentParser(
    description='Visualize 2D vectors as arrows',
    epilog='Example: python main.py --vector "3, 4" --color red'
  )

  parser.add_argument(
    '--vector',
    type=str,
    required=True,
    help='2D vector as comma-seperated values (e.g., "3, 4")'
  )

  parser.add_argument(
    '--output',
    type=str,
    default='outputs/vector_plot.png',
    help='Output file path (default: outputs/vector_plot.png)'
  )

  parser.add_argument(
    '--color',
    type=str,
    default='blue',
    help='Arrow color (default: blue)'
  )

  parser.add_argument(
    '--no-magnitude',
    action='store_true',
    help='Hide magnitude annotation'
  )

  return parser.parse_args()

def parse_vector_string(vector_str: str) -> list:
  """
  Parse comma-seperated vector string into list of floats.

  Args:
    vector_str: String like "3, 4" or "5.5, 2.3"

  Returns:
    List of float values

  Raises:
    ValueError: If string contains non-numeric values
  
  """

  try:
    components = [float(x.strip()) for x in vector_str.split(',')]

    if not components:
      raise ValueError("Vector cannot be empty")
    
    return components
  
  except ValueError as e:
    raise ValueError(
      f"Invalid vector format: '{vector_str}'."
      f"Use comma-seperated numbers like '3, 4'"
    )
  
def main():
  """
  Main CLI execution function.
  
  """

  try:
    # Parse arguments
    args = parse_arguments()

    # Parse vecots
    vector = parse_vector_string(args.vector)

    # Create plot
    plot_vector(
      vector=vector,
      save_path=args.output,
      color=args.color,
      show_magnitude=not args.no_magnitude
    )

    print(f"✓ Vector {vector} plotted successfully")
    print(f"✓ Saved to: {args.output}")

    return 0
  
  except (ValueError, TypeError) as e:
    print(f"Error: {e}", file=sys.stderr)
    print("Try: python main.py --vector \"3, 4\"", file=sys.stderr)
    return 1
  
  except KeyboardInterrupt:
    print("\nCancelled by user", file=sys.stderr)
    return 130
  
if __name__ == '__main__':
    sys.exit(main())
