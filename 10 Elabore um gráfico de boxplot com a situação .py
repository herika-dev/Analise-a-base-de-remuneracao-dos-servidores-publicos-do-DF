import requests
from io import StringIO
import pandas as pd
import matplotlib.pyplot as plt

orig_url = 'https://drive.google.com/file/d/1UrlwBHa47H5lpAkLtDsfuEWfTMQj491X/view?usp=sharing'
file_id = orig_url.split('/')[-2]
dwn_url = 'https://drive.google.com/uc?export=download&id=' + file_id
url_content = requests.get(dwn_url).text
csv_raw = StringIO(url_content)
df_servidores = pd.read_csv(csv_raw, sep=';', low_memory=False)

# Convertendo os valores da coluna LÍQUIDO para  numérico
df_servidores['LÍQUIDO'] = df_servidores['LÍQUIDO'].str.replace(',', '.', regex=False).astype(float)

# Cores personalizadas 
cores = {'boxes': 'green', 'whiskers': 'blue', 'medians': 'red', 'caps': 'black'}

# boxplot com ajustes de espaçamento e rotação
plt.figure(figsize=(12, 8))
bp = df_servidores.boxplot(column='LÍQUIDO', by='SITUAÇÃO', showfliers=False, patch_artist=True, color=cores, vert=False)

#  rótulos e layout do gráfico
plt.title('Remuneração Líquida por Situação do Servidor', fontsize=16)
plt.xlabel('Remuneração Líquida (R$)', fontsize=14)
plt.ylabel('Situação do Servidor', fontsize=14)
plt.xticks(rotation=0, ha='center', fontsize=12)
plt.yticks(fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()