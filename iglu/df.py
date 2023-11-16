# built-in
import os
from pathlib import Path

# 3rd party
import pandas as pd

parent_directory = Path(__file__).parent.absolute()
data_directory = os.path.join(parent_directory, 'data/')

print()

filepath1 = os.path.join(data_directory, 'example_data_1_subject.csv')
filepath2 = os.path.join(data_directory, 'example_data_5_subject.csv')
filepath3 = os.path.join(data_directory, 'example_meal.csv')

example_data_1_subject = pd.read_csv(filepath1, index_col=0)
example_data_5_subject = pd.read_csv(filepath2, index_col=0)
example_meal = pd.read_csv(filepath3, index_col=0)