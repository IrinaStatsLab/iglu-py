import rpy2.robjects as ro
from rpy2.robjects.packages import importr
from rpy2.robjects import pandas2ri

try:
    iglu_r = importr('iglu')
except:
    utils = importr('utils')
    utils.install_packages('file://../data/iglu_3.4.2.tgz', type = "source")
    iglu_r = importr('iglu')

# Pandas DF and R DF share a lot of similarities
# Use this to convert between them: https://rpy2.github.io/doc/v3.5.x/html/generated_rst/pandas.html
def df_conversion(func):
    def inner(*args, **kwargs):
        with (ro.default_converter + pandas2ri.converter).context():
            return func(*args, **kwargs)
    return inner