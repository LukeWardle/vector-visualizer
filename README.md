# Vector Visualizer
A professional Python tool for visualizing 2D vectors as geometric arrows. Built for AI engineers, data scientists, and students learning linear algebra.
## Features
- 🎯 **Single vector visualization** with magnitude annotations
- 🔀 **Multiple vector comparison** on same axes
- 🎨 **Customizable colors** and labels
- 📊 **High-quality output** (300 DPI) for reports and presentations
- ✅ **Comprehensive tests** with pytest
- 📝 **Professional documentation**
## Installation
```bash
# Clone repository
git clone https://github.com/LukeWardle/vector-visualizer.git
cd vector-visualizer
# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
# Install dependencies
pip install -r requirements.txt
```
## Usage
### Command Line
```bash
# Basic usage
python main.py --vector "3,4"
# Custom color and output
python main.py --vector "5,12" --color red --output my_vector.png
# Hide magnitude annotation
python main.py --vector "3,4" --no-magnitude
```
### Python API
```python
from src.plot_utils import plot_vector, plot_multiple_vectors
# Single vector
plot_vector([3, 4], color='blue')
# Multiple vectors
plot_multiple_vectors(
    [[3, 4], [5, 12], [-2, 3]],
    labels=['A', 'B', 'C'],
    colors=['blue', 'red', 'green']
)
```
## Examples
### Vector Addition
```python
a = [3, 2]
b = [1, 4]
c = [a[0] + b[0], a[1] + b[1]]
plot_multiple_vectors(
    [a, b, c],
    labels=['a', 'b', 'a+b'],
    colors=['blue', 'green', 'red']
)
```
## Testing
```bash
pytest -v
```
## Project Structure
```
vector-visualizer/
├── src/
│   └── plot_utils.py      # Core plotting functions
├── tests/
│   └── test_plot_utils.py # Unit tests
├── outputs/               # Generated plots
├── main.py                # CLI interface
├── requirements.txt       # Dependencies
└── README.md             # This file
```
## Technologies
- Python 3.8+
- matplotlib: Professional plotting
- numpy: Numerical computing
- pytest: Testing framework
## Real-World Applications
- **Machine Learning**: Visualizing gradient descent directions
- **Physics**: Force vector decomposition
- **Healthcare**: Patient movement analysis (NHS applications)
- **Transport**: Crowd flow visualization (TfL applications)
- **Education**: Teaching linear algebra concepts
## License
MIT License © 2025 [Your Name]
## Contact
- GitHub: [@LukeWardle](https://github.com/LukeWardle)
- Email: l.wardle@live.co.uk
