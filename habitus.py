import matplotlib.pyplot as plt  # É a principal ferramenta capaz de gerar gráficos no python.
import seaborn as sns            # Baseado no matplotlib o seaborn é uma biblioteca que facilita a criacao de gráficos no
                                 # matplotlib.
import numpy as np               # Estaremos importando o numpy apenas para executar alguns exemplos.
import pandas as pd
"""
Lendo um arquivo .csv com pandas e criando um pandas data frame
"""
import pandas as pd
data = pd.read_csv("prediction.csv")
print(data)
#até aqui ok
plt.figure(figsize=(8, 6))
plt.plot(data['Date'], data['Open'])
plt.xlabel('Date')
plt.ylabel('Open')
plt.title('Petr4_teste')
plt.savefig('annual-real-gnp-us-1909-to-1970.png')


plt.close()