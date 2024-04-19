from setuptools import setup # type: ignore
from Cython.Build import cythonize # type: ignore

setup(ext_modules=cythonize("scheduler2.pyx", compiler_directives={'language_level' : "3"}))