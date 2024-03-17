import requests
from io import StringIO
import pandas as pd
url = 'https://drive.google.com/uc?export=download&id=1UrlwBHa47H5lpAkLtDsfuEWfTMQj491X'
csv_raw = StringIO(requests.get(url).text)
df_servidores = pd.read_csv(csv_raw, sep=';', low_memory=False)

# Filtrando apenas os registros do Corpo de Bombeiros Militar do Distrito Federal e fazendo expressões regulares para 
#correspondência flexível devido existir duas tabelas de corpo de bombeiro diferentes
df_bombeiros = df_servidores[df_servidores['ÓRGÃO'].str.contains(r'CORPO\s+DE\s+BOMBEIROS\s+MILITAR\s+DO\s+DISTRITO\s+FEDERAL', 
case=False) | df_servidores['ÓRGÃO'].str.contains(r'CORPO\s+DE\s+BOMBEIRO\s+MILITAR\s+DO\s+DISTRITO\s+FEDERAL\s+-\s+SIAPE', case=False)]

# Calculaando a quantidade de servidores lotados no Corpo de Bombeiros Militar do Distrito Federal
quantidade_bombeiros = df_bombeiros.shape[0]

# Resultado Resultado
print("Quantidade de servidores lotados no Corpo de Bombeiros Militar do Distrito Federal:", quantidade_bombeiros)