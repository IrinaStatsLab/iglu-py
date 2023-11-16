# built-in
import os
from pathlib import Path

# 3rd party
from dotenv import load_dotenv
import rpy2.robjects as ro
from rpy2.robjects.packages import importr
from rpy2.robjects import pandas2ri

# global instance of r-version of iglu
iglu_r = None

def import_iglu(filepath: str = None) -> None:
    ''' Attempts to load `iglu` already installed on machine.

        If it can't find it, it uses `install_iglu`. See that function for more specific instructions.
    '''
    global iglu_r

    try:
        iglu_r = importr('iglu')

    except:
        install_iglu(filepath)
        iglu_r = importr('iglu')

def install_iglu(filepath: str = None) -> None:
    ''' Install the `iglu` R package from a tar.gz file on your machine.

        `filepath` is either of the options below:
        1. "iglu" to download latest version from CRAN
        2. None: uses the tar.gz file specified by `.env`, which comes bundled with `iglu-py`. (Note: this file resides in the same directory as the `.env` file itself)
        3. Absolute file path to the tar.gz iglu source file on your machine

        Remember to call "import_iglu()" after "install_iglu()" if you want to use it.
    '''

    print('Attempting to install iglu-r now (~20 seconds).')
    
    try:
        if filepath == None:
            # get file path
            load_dotenv()

            parent_directory = Path(__file__).parents[1].absolute()
            filepath = os.path.join(parent_directory, os.getenv("IGLU_FILE_NAME"))

        # install package
        utils = importr('utils')
        utils.install_packages(filepath, type = "source")

        print('R-version of iglu successfully installed. You are free to proceed.\n\n')
    
    except Exception as error:
        print(f'The following error was encountered: {error}')

def uninstall_iglu():
    print('Attempting to uninstall the R version of iglu from your system.')

    try:
        utils = importr('utils')
        utils.remove_packages('iglu')

        global iglu_r
        iglu_r = None

    except Exception as error:
        print(f'The following error was encountered: {error}')

def df_conversion(func):
    ''' 
        Pandas DF and R DF share a lot of similarities but not all

        Use this decorator to convert between them:
        - Adapted from: https://rpy2.github.io/doc/v3.5.x/html/generated_rst/pandas.html
        - What are decorators?: https://youtu.be/BE-L7xu8pO4?si=2GCzN6LWSm5cKQ81
        - See "metrics.py" for examples
    '''
    def inner(*args, **kwargs):
        with (ro.default_converter + pandas2ri.converter).context():
            return func(*args, **kwargs)
    return inner