import requests
from io import StringIO
import pandas as pd

orig_url = 'https://drive.google.com/file/d/1UrlwBHa47H5lpAkLtDsfuEWfTMQj491X/view?usp=sharing'
file_id = orig_url.split('/')[-2]
dwn_url = 'https://drive.google.com/uc?export=download&id=' + file_id
url = requests.get(dwn_url).text
csv_raw = StringIO(url)
df_servidores = pd.read_csv(csv_raw, sep=';', low_memory=False)

# todas as funções únicas da coluna FUNÇÃO 
todas_funcoes = df_servidores['FUNÇÃO'].unique()

# Imprimir todos os resultados
print("Lista de todas as funções contidas na base de dados:")
for funcao in todas_funcoes:
    print(funcao)
