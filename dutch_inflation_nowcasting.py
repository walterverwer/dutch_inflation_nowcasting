import os
import pandas as pd
import numpy as np


# Set-up data
DATA = 'dutch_inflation.csv'
path = os.path.join('.', 'data', DATA)
raw_data = pd.read_csv(path, sep=';')


