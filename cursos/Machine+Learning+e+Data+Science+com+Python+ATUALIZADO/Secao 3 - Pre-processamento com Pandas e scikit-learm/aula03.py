
# Loading Package
import sklearn
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import Imputer
import pandas as pd


# Loading Data
base = pd.read_csv(
    'Secao 3 - Pre-processamento com Pandas e scikit-learm/credit_data.csv')

# Find missing values
print(pd.isnull(base['age']))

# or
print(base.loc[pd.isnull(base['age'])])

prevition = base.iloc[:, 1:4].values

print(prevition)

classe = base.iloc[:, 4].values
print(classe)


# Loading Package

imputer = Imputer(missing_values="NaN", strategy="mean", axis=0)
imputer = imputer.fit(prevition[:, 0:3])

prevition[:0:3] = imputer.transform(prevition[:, 0:3])

# Find missing values
print(prevition)
