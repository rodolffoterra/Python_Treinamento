
# Loading Package
import pandas as pd

# Loading Data
base = pd.read_csv(
    'credit_data.csv')

# Analytics describe
print(base.describe())
