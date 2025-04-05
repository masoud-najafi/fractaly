# Fractaly - Fractal Visualization Tool

![Fractal Example](doc/images/mandelbrot.png)

A cross-platform application for generating and exploring fractal images.

## Features
- Multiple fractal types (Mandelbrot, Julia, etc.)
- Interactive zoom/pan
- Custom color schemes

## Installation
```bash
git clone https://github.com/masoud-najafi/fractaly
cd fractaly
pip install -e .  # in development mode
#or
pip install  .    # in production mode
```

## Usage in Python
```python
import wx
import fractaly
app = wx.App(False)
frame = fractaly.FractalFrame()
frame.Show()
app.MainLoop()
```

## usage using Python entry point
python -m fractaly

## Git structure
```
fractaly/
├── .gitignore
├── LICENSE.txt
├── README.md
├── pyproject.toml          # Build system config
├── setup.py         
├── setup_cx_Freeze.py          
├── requirements.txt  # Dev dependencies and # product Runtime dependencies
│
├── src/                    # Application source
│   └── fractaly/
│       ├── py.typed
│       ├── __init__.py
│       ├── __main__.py
│       ├── algorithms/     # Fractal implementations
│       │   ├── __init__.py
│       │   └── core1.py
│       ├── core/     # Fractal implementations
│       │   ├── fractal_maths.c
│       │   └── test_fractal_maths.py
│       ├── gui/  # Rendering
│       │   ├── __init__.py
│       │   └── core2.py
│       └── lib/       # Platform-specific
│           ├── win64/
│           │   └── fractal_maths.dll
│           └── linux64/
│               └── libfractal_maths.so
│
└── doc/                   # Documentation
    └── tutorial.md
```
##Build/installation

Key Techniques Used
Underscore prefix:
1)_internal directory name indicates it's private
2)_PrivateClass name indicates it's internal

Controlled exports:
1)__all__ in root __init__.py specifies what gets imported with from package import *
2)Only explicitly import the public class in root __init__.py

Python module system:
1)The package structure naturally hides implementation details
2)Internal imports use relative imports (.internal)


Version synchronization: Keep __version__, setup.py version, and pyproject.toml version in sync.

Type checking: The empty py.typed file indicates to type checkers (like mypy) that your package has type information.

Modern vs traditional:
pyproject.toml is the modern standard (PEP 621)
setup.py is still widely used and may be needed for some cases

Installation:
For development: pip install -e .
For production: pip install .

Publishing:
Build: python -m build
Upload to PyPI: twine upload dist/*