from setuptools import setup, find_packages

VERSION = '0.0.0' 
DESCRIPTION = 'Python version of R package `iglu`. Wraps the R functions, making them accessible in Python.'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name='iglu_py', 
        version=VERSION,
        author='Nathaniel J. Fernandes; Irina Gaynanova',
        author_email='njfernandes24@tamu.edu; irinag@umich.edu',
        description=DESCRIPTION,
        packages=find_packages(),
        install_requires=['rpy2', 'pandas'],        
        keywords=['iglu', 'wrapper'],
)