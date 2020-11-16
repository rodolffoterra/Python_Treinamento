
# Loading Package
import pandas as pd

# Loading Data
base = pd.read_csv(
    'Secao 3 - Pre-processamento com Pandas e scikit-learm/credit_data.csv')

# Analytics describe
print(base.describe())
