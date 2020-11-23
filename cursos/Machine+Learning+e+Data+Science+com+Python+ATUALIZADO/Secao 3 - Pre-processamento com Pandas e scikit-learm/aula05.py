
# Loading Package
from sklearn.preprocessing import LabelEncoder

# Loading Data
base = pd.read_csv(
    'Secao 3 - Pre-processamento com Pandas e scikit-learm/census.csv')

# Names Columns
print(base.columns.values)


previsores = base.iloc[:, 0:14].values
classe = base.iloc[:, 14].values

print(" Df Previsores")
print(previsores)
print(" Df classe")
print(classe)


labelencoder_previsorers = LabelEncoder()


# Convert catechetical variable in numeric
# label = labelencoder_previsorers.fit_transform(previsores[,1])

previsores[:, 1] = labelencoder_previsorers.fit_transform(previsores[:, 1])
previsores[:, 3] = labelencoder_previsorers.fit_transform(previsores[:, 3])
previsores[:, 5] = labelencoder_previsorers.fit_transform(previsores[:, 5])
previsores[:, 6] = labelencoder_previsorers.fit_transform(previsores[:, 6])
previsores[:, 7] = labelencoder_previsorers.fit_transform(previsores[:, 7])
previsores[:, 8] = labelencoder_previsorers.fit_transform(previsores[:, 8])
previsores[:, 9] = labelencoder_previsorers.fit_transform(previsores[:, 9])
previsores[:, 13] = labelencoder_previsorers.fit_transform(previsores[:, 13])

print(previsores[:, 9])
print(previsores[:, 5])

# Variable kind Dummy

#onehotencoder = OneHotEncoder(categorical_features=[8])
#previsores = onehotencoder.fit_transform(previsores).toarray()
