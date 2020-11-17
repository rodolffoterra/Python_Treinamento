
# Loading Package
import pandas as pd
from sklearn.preprocessing import StandardScaler


# Loading Data
base = pd.read_csv(
    'credit_data.csv')

# Normalization
scaler = StandardScaler()
previsores = scaler.fit_transform(base)

print(previsores)
