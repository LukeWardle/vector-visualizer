"""
Unit tests for plot_utils module.

"""

import pytest
import os
from src.plot_utils import plot_vector, plot_multiple_vectors

# Test fixtures
@pytest.fixture
def temp_output_dir(tmp_path):
  """
  Create temporary output directory for tests.
  
  """
  output_dir = tmp_path / "test_outputs"
  output_dir.mkdir()
  return str(output_dir)

# Test for plot_vector
def test_plot_vector_basic(temp_output_dir):
  """
  Test basic vector plotting.
  
  """
  output_path = os.path.join(temp_output_dir, "test_vector.png")
  plot_vector([3, 4], save_path=output_path)
  assert os.path.exists(output_path)

def test_plot_vector_zero(temp_output_dir):
  """
  Test plotting zero vector.
  
  """
  output_path = os.path.join(temp_output_dir, "zero_vector.png")
  plot_vector([0, 0], save_path=output_path)
  assert os.path.exists(output_path)

def test_plot_vector_negative(temp_output_dir):
  """
  Test vector with negative vectors.
  
  """
  output_path = os.path.join(temp_output_dir, "negative.png")
  plot_vector([-3, -4], save_path=output_path)
  assert os.path.exists(output_path)

def test_plot_vector_wrong_dimension():
  """
  Test error handling for wrong dimension.
  
  """
  with pytest.raises(ValueError, match="must be 2D"):
    plot_vector([1, 2, 3])

# Tests for plot_multiple_vectors
def test_plot_multiple_vectors_basic(temp_output_dir):
  """
  Test plotting multiple vectors.
  
  """
  output_path = os.path.join(temp_output_dir, "multiple.png")
  plot_multiple_vectors(
    [[3, 4], [5, 12]],
    save_path=output_path
  )
  assert os.path.exists(output_path)

def test_plot_multiple_with_labels(temp_output_dir):
    """Test multiple vectors with custom labels."""
    output_path = os.path.join(temp_output_dir, "labeled.png")
    plot_multiple_vectors(
        [[3, 4], [5, 12]],
        labels=['A', 'B'],
        colors=['red', 'blue'],
        save_path=output_path
    )
    assert os.path.exists(output_path)
def test_plot_multiple_empty_list():
    """Test error handling for empty vector list."""
    with pytest.raises(ValueError, match="at least one vector"):
        plot_multiple_vectors([])
def test_plot_multiple_wrong_dimension():
    """Test error handling for non-2D vectors."""
    with pytest.raises(ValueError, match="All must be 2D"):
        plot_multiple_vectors([[3, 4], [1, 2, 3]])
