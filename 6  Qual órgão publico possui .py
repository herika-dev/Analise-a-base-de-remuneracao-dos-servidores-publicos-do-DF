import requests
from io import StringIO
import pandas as pd

orig_url='https://drive.google.com/file/d/1UrlwBHa47H5lpAkLtDsfuEWfTMQj491X/view?usp=sharing'


file_id = orig_url.split('/')[-2]
dwn_url='https://drive.google.com/uc?export=download&id=' + file_id
url = requests.get(dwn_url).text
csv_raw = StringIO(url)
df_servidores = pd.read_csv(csv_raw,sep=';',low_memory=False)

df_servidores['BRUTO'] = df_servidores['BRUTO'].str.replace(',', '.').astype(float)
# Calculando a média salarial de  cada órgão público
media_salarial_por_orgao = df_servidores.groupby('ÓRGÃO')['BRUTO'].mean()

# órgão público com a maior média salarial
orgao_maior_media_salarial = media_salarial_por_orgao.idxmax()

# Resultado maior média salarial
maior_media_salarial = media_salarial_por_orgao.max()

print("O órgão público com a maior média salarial é:", orgao_maior_media_salarial)
print("A maior média salarial é:", maior_media_salarial)
