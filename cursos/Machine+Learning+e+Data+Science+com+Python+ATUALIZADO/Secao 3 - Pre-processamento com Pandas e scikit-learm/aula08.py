# Loading Package

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
import pandas as pd
import numpy as np


# Loading Data
base = pd.read_csv(
    'credit_data.csv')

# Remove age for mean Age
base.loc[base.age < 0, 'age'] = 40.92

previsores = base.iloc[:, 1:4].values
classe = base.iloc[:, 4].values

# Remove num,ber missing
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer = imputer.fit(previsores[:, 1:4])
previsores[:, 1:4] = imputer.transform(previsores[:, 1:4])

# Standardization
scaler = StandardScaler()
previsores = scaler.fit_transform(previsores)

# create data Train and Test

previsores_treinamento, previsores_teste, classe_treinamento, classe_teste = train_test_split(
    previsores, classe, test_size=0.25, random_state=0)

print("previsores_treinamento")
print(previsores_treinamento.shape)

print("previsores_teste")
print(previsores_teste.shape)

print('classe_treinamento')
print(classe_treinamento.shape)

print('classe_teste')
print(classe_teste.shape)
