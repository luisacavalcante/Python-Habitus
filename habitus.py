import matplotlib.pyplot as plt  # É a principal ferramenta capaz de gerar gráficos no python.
import seaborn as sns            # Baseado no matplotlib o seaborn é uma biblioteca que facilita a criacao de gráficos no
                                 # matplotlib.
import numpy as np               # Estaremos importando o numpy apenas para executar alguns exemplos.
import pandas as pd
"""
Lendo um arquivo .csv com pandas e criando um pandas data frame
"""
import pandas as pd
data = pd.read_csv("data.txt")
print(data)
#até aqui ok
plt.figure(figsize=(8, 6))
plt.plot(data['horario'], data['x'])
plt.xlabel('horario')
plt.ylabel('x')
plt.title('Habitus eixo X')
plt.savefig('Habitus-eixo-x.png')

plt.figure(figsize=(8, 6))
plt.plot(data['horario'], data['y'])
plt.xlabel('horario')
plt.ylabel('y')
plt.title('Habitus eixo y')
plt.savefig('Habitus-eixo-y.png')

plt.figure(figsize=(8, 6))
plt.plot(data['horario'], data['z'])
plt.xlabel('horario')
plt.ylabel('z')
plt.title('Habitus eixo Z')
plt.savefig('Habitus-eixo-z.png')

plt.close()
