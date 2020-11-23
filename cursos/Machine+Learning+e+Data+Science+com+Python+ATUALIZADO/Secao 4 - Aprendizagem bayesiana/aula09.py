# Load packahe
 
import pandas as pd 
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder

# Load the data
base = pd.read_csv('risco_credito.csv')

previsores = base.iloc[:,0:4].values
classe = base.iloc[:,4].values

labelencoder = LabelEncoder()
previsores[:,0] = labelencoder.fit_transform(previsores[:,0])
previsores[:,1] = labelencoder.fit_transform(previsores[:,1])
previsores[:,2] = labelencoder.fit_transform(previsores[:,2])
previsores[:,3] = labelencoder.fit_transform(previsores[:,3])


classificador = GaussianNB()
classificador.fit(previsores, classe)

# hitórico boa, dívida alta, garantia nenhuma, renda > 35
resultado = classificador.predict([[0,0,1,2]])
print('hitórico boa, dívida alta, garantia nenhuma, renda > 35 - Resulta:',resultado)

# histórica ruim, dívida alta, garantida adequada, renda < 15
resultado = classificador.predict([[3,0,0,0]])
print('histórica ruim, dívida alta, garantida adequada, renda < 15:',resultado)

print("Tipos de classes")
print(classificador.classes_)

print("Contagem de cada tipo de classes")
print(classificador.class_count_)

print("Probabilidade apriori da classes")
print(classificador.class_prior_)



