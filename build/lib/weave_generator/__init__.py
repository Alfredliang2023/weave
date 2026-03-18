"""
Weave Generator - 纺织组织生成器库

一个用于生成各种纺织组织结构的 Python 库，支持 9 种常见的组织类型。
"""

from .unified_interface import WeaveGenerator, generate_weave, get_weave_types

__version__ = "1.0.0"
__all__ = ["WeaveGenerator", "generate_weave", "get_weave_types"]

__author__ = "Weave Generator Team"
__license__ = "MIT"
