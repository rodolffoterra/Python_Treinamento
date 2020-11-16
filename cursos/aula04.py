
# Loading Package
import pandas as pd
from sklearn.preprocessing import StandardScaler


# Loading Data
base = pd.read_csv(
    'Secao 3 - Pre-processamento com Pandas e scikit-learm/credit_data.csv')

# Normalization
scaler = StandardScaler()
previsores = scaler.fit_transform(base)

print(previsores)
