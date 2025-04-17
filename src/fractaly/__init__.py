#from .core1 import FractalFrame
from fractaly.algorithm.core1 import FractalFrame, maincaller

__version__ = "0.2.0"  # Follow semantic versioning
__all__ = ['FractalFrame','maincaller']  # Only expose Public Classes to import *
# __all__ in root __init__.py specifies what gets imported with from package import *
# Only explicitly import the public class in root __init__.py