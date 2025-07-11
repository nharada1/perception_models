"""
Perception Models Package

A collection of perception models and tools for computer vision tasks.
"""

__version__ = "1.0.0"

# Import main modules
from . import core
from . import apps

# Make main modules available at package level
__all__ = ["core", "apps", "__version__"]
