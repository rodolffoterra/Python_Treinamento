
# Loading Package
import pandas as pd

# Loading Data
base = pd.read_csv(
    'Secao 3 - Pre-processamento com Pandas e scikit-learm/credit_data.csv')

# find Variable
print(base.loc[base['age'] < 0])

# (1) Drop Colunms

base.drop('age', 1, inplace=True)

print(base.head())

#################################
# Loading Data
base = pd.read_csv(
    'Secao 3 - Pre-processamento com Pandas e scikit-learm/credit_data.csv')

print(base.shape)

# (2) Remove only negative numbers
base.drop(base[base.age < 0].index, inplace=True)

print(base.shape)


# Loading Data
base = pd.read_csv(
    'Secao 3 - Pre-processamento com Pandas e scikit-learm/credit_data.csv')

print(base.shape)

#################################

# (3) Correct padding manually _ mean

base['age'][base.age > 0].mean()
base.loc[base.age < 0, 'age'] = 40.92

# find Variable
print(base.loc[base['age'] < 0])
