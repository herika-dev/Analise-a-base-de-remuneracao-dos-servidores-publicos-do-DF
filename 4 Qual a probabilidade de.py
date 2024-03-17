import requests
from io import StringIO
import pandas as pd

orig_url = 'https://drive.google.com/file/d/1UrlwBHa47H5lpAkLtDsfuEWfTMQj491X/view?usp=sharing'
file_id = orig_url.split('/')[-2]
dwn_url = 'https://drive.google.com/uc?export=download&id=' + file_id
url_content = requests.get(dwn_url).text
csv_raw = StringIO(url_content)
df_servidores = pd.read_csv(csv_raw, sep=';', low_memory=False)

# Calculando o número de linhas da Secretaria de Educação
numero_linhas_secretaria_educacao = len(df_servidores[df_servidores['ÓRGÃO'].str.contains('SECRETARIA DE ESTADO DE EDUCACAO                                                ', case=False)])
total_linhas_dataset = len(df_servidores)

# probabilidade em porcentagem
probabilidade = (numero_linhas_secretaria_educacao / total_linhas_dataset) * 100
probabilidade_formatada = "{:.2f}%".format(probabilidade)
# Resultado de probabilidade 
print("Probabilidade de escolher uma linha da Secretaria de Educação:", probabilidade_formatada)