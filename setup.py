from setuptools import setup, find_packages

VERSION = "1.0.6"
DESCRIPTION = "Python wrapper of R package `iglu` for continuous glucose monitoring data analysis. Wraps the R functions, thus making them accessible in Python."

# read the contents of your README file
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

# Setting up
setup(
    name="iglu-py",  # name must match the folder name where code lives
    version=VERSION,
    author="Nathaniel J. Fernandes, Lizzie Chun, Irina Gaynanova",
    author_email="njfernandes24@tamu.edu, lizzie_chun1@tamu.edu, irinagn@umich.edu",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "rpy2>=3.5.13",
        "pandas>=2.0.0",
    ],  # we've validated functionality with these package versions.
    python_requires=">=3.8.0",
    keywords=["iglu", "Continuous Glucose Monitoring analysis software", "diabetes"],
    include_package_data=True,
)
