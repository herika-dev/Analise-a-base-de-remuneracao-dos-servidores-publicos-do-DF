import requests
from io import StringIO
import pandas as pd
import matplotlib.pyplot as plt

orig_url = 'https://drive.google.com/file/d/1UrlwBHa47H5lpAkLtDsfuEWfTMQj491X/view?usp=sharing'
file_id = orig_url.split('/')[-2]
dwn_url = 'https://drive.google.com/uc?export=download&id=' + file_id
url = requests.get(dwn_url).text
csv_raw = StringIO(url)
df_servidores = pd.read_csv(csv_raw, sep=';', low_memory=False)

df_servidores['BRUTO'] = df_servidores['BRUTO'].str.replace(',', '.')

# Convertendo os valores da coluna 'BRUTO' para números de ponto flutuante
df_servidores['BRUTO'] = df_servidores['BRUTO'].astype(float)

# Agrupaando os dados por órgão e calcular a soma da remuneração bruta para cada órgão
remuneracao_por_orgao = df_servidores.groupby('ÓRGÃO')['BRUTO'].sum()

# Definindo um limite para agrupar órgãos com valores baixos em uma categoria "Outros"
limite = 1000000
outros = remuneracao_por_orgao[remuneracao_por_orgao < limite].sum()
remuneracao_por_orgao = remuneracao_por_orgao[remuneracao_por_orgao >= limite]
remuneracao_por_orgao['Outros'] = outros

# Preparando gráfico de pizza
fig, ax = plt.subplots(figsize=(14, 8))  # Aumentar o tamanho da figura
patches, _, _ = ax.pie(remuneracao_por_orgao, startangle=140, autopct='%1.1f%%')
plt.axis('equal')  # Equal aspect ratio garante que o gráfico seja um círculo
plt.title('Remuneração Bruta dos Servidores por Órgão', fontsize=16)
# Criaando uma legenda separada para os órgãos
legend_labels = [f'{orgao}: R$ {remuneracao:,.2f}' for orgao, remuneracao in zip(remuneracao_por_orgao.index, remuneracao_por_orgao.values)]
plt.legend(patches, legend_labels, loc="center left", fontsize='medium', title='Órgão:       Remuneração', bbox_to_anchor=(1, 0.5), labelspacing=1.2)

plt.show()