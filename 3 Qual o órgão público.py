import requests
from io import StringIO
import pandas as pd

orig_url = 'https://drive.google.com/file/d/1UrlwBHa47H5lpAkLtDsfuEWfTMQj491X/view?usp=sharing'
file_id = orig_url.split('/')[-2]
dwn_url = 'https://drive.google.com/uc?export=download&id=' + file_id
url = requests.get(dwn_url).text
csv_raw = StringIO(url)
df_servidores = pd.read_csv(csv_raw, sep=';', low_memory=False)


# calculando o número de funcionários por órgão
num_funcionarios_por_orgao = df_servidores['ÓRGÃO'].value_counts()

# órgão público com maior número de funcionários
orgao_maior_numero_funcionarios = num_funcionarios_por_orgao.idxmax()
numero_funcionarios = num_funcionarios_por_orgao.max()

print("Órgão público com o maior número de funcionários:", orgao_maior_numero_funcionarios)
print("Número de funcionários:", numero_funcionarios)
