from setuptools import setup, find_packages

VERSION = '0.0.0' 
DESCRIPTION = 'Python wrapper of R package `iglu`. Wraps the R functions, making them accessible in Python.'

# Setting up
setup(
        name='iglu', # name must match the folder name where code lives
        version=VERSION,
        author='Lizzie Chun, Nathaniel J. Fernandes, Irina Gaynanova', # TODO: proper acknowledgement
        author_email='lizzie_chun1@tamu.edu, njfernandes24@tamu.edu, irinagn@umich.edu', 
        description=DESCRIPTION,
        packages=find_packages(),
        install_requires=['rpy2==3.5.13', 'pandas==2.1.2', 'python-dotenv==1.0.0'], # we've validated functionality with these package versions.     
        keywords=['iglu', 'wrapper'],
)