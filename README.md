# Fractaly - Fractal Visualization Tool

![Fractal Example](doc/images/mandelbrot.png)

A cross-platform application for generating and exploring fractal images.

## Features
- Multiple fractal types (Mandelbrot, Julia, etc.)
- Interactive zoom/pan
- Custom color schemes

##downlod
use can directly install fractaly from PyPI 
https://pypi.org/project/fractaly/
```bash
pip install fractaly     #install fractaly
pip uninstall fractaly   #uninstall fractaly
```

## Install the full source code from github
```bash
git clone https://github.com/masoud-najafi/fractaly
cd fractaly
#instal in development mode 
pip install -e . 
#or install in production mode
pip install  .  

#if you need to build the code
python -m build
#to publish it on PyPI
python -m twine upload --verbose dist/* 
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
```bash
python -m fractaly
```

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

Key Techniques Used<br>
Underscore prefix:<br>
1)_internal directory name indicates it's private<br>
2)_PrivateClass name indicates it's internal<br>
<br>
Controlled exports:<br>
1)__all__ in root __init__.py specifies what gets imported with from package import *<br>
2)Only explicitly import the public class in root __init__.py<br>
<br>
Python module system:<br>
1)The package structure naturally hides implementation details<br>
2)Internal imports use relative imports (.internal)<br>
<br>

Version synchronization: Keep __version__, setup.py version, and pyproject.toml version in sync.<br>
<br>
Type checking: The empty py.typed file indicates to type checkers (like mypy) that your package has type information.<br>
<br>
Modern vs traditional:<br>
pyproject.toml is the modern standard (PEP 621)<br>
setup.py is still widely used and may be needed for some cases<br>
<br>
Installation:<br>
For development: pip install -e .<br>
For production: pip install .<br>
<br>
Publishing:<br>
Build: python -m build<br>
Upload to PyPI: twine upload dist/*<br>