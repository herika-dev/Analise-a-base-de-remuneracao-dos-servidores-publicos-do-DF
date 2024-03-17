import requests
from io import StringIO
import pandas as pd

orig_url = 'https://drive.google.com/file/d/1UrlwBHa47H5lpAkLtDsfuEWfTMQj491X/view?usp=sharing'
file_id = orig_url.split('/')[-2]
dwn_url = 'https://drive.google.com/uc?export=download&id=' + file_id
url = requests.get(dwn_url).text
csv_raw = StringIO(url)
df_servidores = pd.read_csv(csv_raw, sep=';', low_memory=False)

df_servidores['REMUNERAÇÃO BÁSICA'] = df_servidores['REMUNERAÇÃO BÁSICA'].str.replace(',', '.').astype(float)

# maior remuneração básica
maior_remuneracao = df_servidores.loc[df_servidores['REMUNERAÇÃO BÁSICA'].idxmax()]

# órgão e o valor da maior remuneração básica
print("Órgão com a maior remuneração básica:", maior_remuneracao['ÓRGÃO'])
print("Valor da maior remuneração básica:", maior_remuneracao['REMUNERAÇÃO BÁSICA'])
