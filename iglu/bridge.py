# built-in
import os
from pathlib import Path

# 3rd party
from dotenv import load_dotenv
import rpy2.robjects as ro
from rpy2.robjects.packages import importr
from rpy2.robjects import pandas2ri

try:
    iglu_r = importr('iglu')
except:
    # will take longer (~20 sec) b/c downloading package
    print('`iglu` R package not found on system. Installing now (~20 seconds).')
    
    # get file path
    load_dotenv()

    parent_directory = Path(__file__).parent.absolute()
    file_name = os.path.join(parent_directory, os.getenv("IGLU_FILE_NAME"))
    print(parent_directory, file_name)

    # install package
    utils = importr('utils')
    utils.install_packages(file_name, type = "source")
    iglu_r = importr('iglu')

def df_conversion(func):
    ''' 
        Pandas DF and R DF share a lot of similarities
        Use this decorator to convert between them:
        - Adapted from: https://rpy2.github.io/doc/v3.5.x/html/generated_rst/pandas.html
        - What are decorators?: https://youtu.be/BE-L7xu8pO4?si=2GCzN6LWSm5cKQ81
    '''
    def inner(*args, **kwargs):
        with (ro.default_converter + pandas2ri.converter).context():
            return func(*args, **kwargs)
    return inner