# import package Panda

import pandas as pd

import numpy as np

# creade u nupy.array

data =np.array([['Portugal', 'Lisboa', 10000000],
                    ['Peru', 'Lima', 32000000],
                    ['Chile', 'Santiago', 18000000],
                    ['Brasil', 'Brasília', 209000000]])

df = pd.DataFrame(data, index=range(100,104),columns=['País', 'Capital', 'População'])

print(type(df))
print(df)