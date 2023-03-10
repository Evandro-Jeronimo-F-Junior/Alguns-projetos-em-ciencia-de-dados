import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Criando as datas com for
# fis um map, mas nem precisava. Fiz mais pra treinar o map msm, no caso até podia por direto no DataFrame.

anos = list(range(2000, 2024))
anos = list(map(str, anos))
np.random.seed(40)

#Criando um DataFrame usando a biblioteca numpy    Obs: criei o indice, mas não precisava

df = pd.DataFrame({
    'Ano': anos,
    'Indice': np.arange(0, 24),
    'Código do produto': list(np.random.randint(2, size=(24, 7))),
    'Genero Comprou': np.random.choice(['M', 'F'], size=24),
    'Fabricar produto': np.random.randint(-30, 0, size=24),
    'Lucro Bruto': np.random.randint(30, 300, size=24),
    'Lucro Liquido': np.random.randint(0, 2, size=24),
    })

#Editando algumas cilunas e suas repectivas linhas

df['Valor venda com disconto'] = np.random.choice([0.9, 0.8, 0.7], size=24) * df['Lucro Bruto']
df['Lucro Liquido'] = df['Valor venda com disconto'] + df['Fabricar produto']

#criando os graficos com suplots

fig, axs = plt.subplots(nrows=2, ncols=2)

#primeiro Grafico

primeiro_grafico = df.plot(x='Ano', y='Lucro Liquido', ax=axs[0, 0], figsize=(18, 9), color='red')
primeiro_grafico.set_xlabel('Ano')
primeiro_grafico.set_ylabel('Lucro Total')
primeiro_grafico.set_title('Lucro por ano')

#segundo grafico

segundo_grafico = df.plot(x='Ano', y='Valor venda com disconto', color='green', ax=axs[0, 1])
segundo_grafico.set_xlabel('Ano')
segundo_grafico.set_ylabel('Valor da venda com discontos')
segundo_grafico.set_title('Vendas por ano com discontos')

#terceiro grafico

axs[1, 0].plot(df.loc[:9, 'Ano'], df.loc[:9, 'Fabricar produto'])
axs[1, 0].set_xlabel('Ano')
axs[1, 0].set_ylabel('Fabricar produto')
axs[1, 0].set_title('Custos de Fabricar produtos por ano')

#quarto grafico

x = df['Lucro Liquido']
y1 = np.random.randint(df['Genero Comprou'].value_counts()['M'], df['Genero Comprou'].value_counts()['M'] + 1, size=24)
y2 = np.random.randint(df['Genero Comprou'].value_counts()['F'], df['Genero Comprou'].value_counts()['F'] + 1, size=24)
axs[1, 1].bar(x, y1, color='blue', alpha=0.5, label='y1', width=5, align='edge')
axs[1, 1].set_ylabel('Masculino (preto)')

#criando um segundo y

ax2 = axs[1, 1].twinx()
ax2.bar(x, y2, color='black', alpha=0.5, label='y2', width=5, align='edge')
ax2.set_ylabel('Feminino (azul)')

#ajustando a escala

axs[1, 1].set_ylim(0, max(y1.max(), y2.max()) * 1.05)
ax2.set_ylim(0, max(y1.max(), y2.max()) * 1.05)
axs[1, 1].set_title('Valor gasto por genero')

#ajustando um pouco o plot

plt.subplots_adjust(wspace=0.4, hspace=0.4)
plt.show()
