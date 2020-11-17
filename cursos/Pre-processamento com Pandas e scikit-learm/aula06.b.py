# Loading Package
from sklearn.preprocessing import LabelEncoder
import pandas as pd

# Loading Data
base = pd.read_csv(
    'census.csv')

# Variable Dumming for columns "target"

previsores = base.iloc[:, 1:14].values
classe = base.iloc[:, 14].values

labelenconder_previsores = LabelEncoder()

labelenconder_classes = LabelEncoder()
classe = labelenconder_classes.fit_transform(classe)

print(classe)
