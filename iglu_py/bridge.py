# built-in
import os
from pathlib import Path

# 3rd party
import rpy2.robjects as ro
from rpy2.robjects.packages import importr
from rpy2.robjects import pandas2ri

# global instance of r-version of iglu
iglu_r = None
IGLU_TGZ_NAME = "iglu_4.0.0.tar.gz"


def import_iglu(install_name: str = IGLU_TGZ_NAME) -> None:
    """Attempts to load `iglu` already installed on machine.

    If it can't find it, it passes `install_iglu` the specified `install_name` argument. See that function for more specific instructions.
    """
    global iglu_r

    try:
        iglu_r = importr("iglu")

    except:
        install_iglu(install_name)
        iglu_r = importr("iglu")


def install_iglu(name: str = IGLU_TGZ_NAME, name_type="relative") -> None:
    """Install the `iglu` R package from a tar.gz file on your machine.

    (`name`, `name_type`) combinations are either of the options below
    1. ('iglu', 'CRAN'): to download latest version from CRAN
    2. (File specified in "IGLU_TGZ_NAME" variable, 'relative'): uses the tar.gz file specified, relative to the package working directory. (Note: specified version comes bundled with iglu-py)
    3. (path/to/file, 'absolute'): Absolute file path to the tar.gz iglu source file on your machine

    Remember to call "import_iglu()" after "install_iglu()" if you want to use it.
    """

    if name_type not in ["CRAN", "relative", "absolute"]:
        raise ValueError(
            f'name_type should be one of "CRAN", "relative", or "absolute". Got: {name_type}'
        )

    print("Attempting to install iglu-r now (~20 seconds).")

    dependencies = [
        "caTools",
        "dplyr",
        "DT",
        "ggplot2",
        "ggpubr",
        "gridExtra",
        "hms",
        "lubridate",
        "magrittr",
        "patchwork",
        "pheatmap",
        "scales",
        "shiny",
        "tibble",
        "tidyr",
        "zoo",
        "gtable",
        "plotly",
    ]

    try:
        utils = importr("utils")

        for dependency in dependencies:
            utils.install_packages(
                dependency, method="wget", repos="https://cloud.r-project.org/"
            )

        if name_type == "CRAN":
            utils.install_packages(
                name, method="wget", repos="https://cloud.r-project.org/"
            )

        if name_type == "relative":
            # get file path
            parent_directory = Path(__file__).parent.absolute()
            filepath = os.path.join(parent_directory, name)

            print(parent_directory, Path(__file__), filepath)

            utils.install_packages(filepath, type="source")

        if name_type == "absolute":
            utils.install_packages(name, type="source")

        print("R-version of iglu successfully installed. You are free to proceed.\n\n")

    except Exception as error:
        print(f"The following error was encountered: {error}")


def uninstall_iglu():
    print("Attempting to uninstall the R version of iglu from your system.")

    try:
        utils = importr("utils")
        utils.remove_packages("iglu")

        global iglu_r
        iglu_r = None

    except Exception as error:
        print(f"The following error was encountered: {error}")


def df_conversion(func):
    """
    Pandas DF and R DF share a lot of similarities but not all

    Use this decorator to convert between them:
    - Adapted from: https://rpy2.github.io/doc/v3.5.x/html/generated_rst/pandas.html
    - What are decorators?: https://youtu.be/BE-L7xu8pO4?si=2GCzN6LWSm5cKQ81
    - See "metrics.py" for examples
    """

    def inner(*args, **kwargs):
        with (ro.default_converter + pandas2ri.converter).context():
            return func(*args, **kwargs)

    return inner
