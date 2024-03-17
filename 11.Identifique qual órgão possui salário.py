import requests
from io import StringIO
import pandas as pd


orig_url = 'https://drive.google.com/file/d/1UrlwBHa47H5lpAkLtDsfuEWfTMQj491X/view?usp=sharing'
file_id = orig_url.split('/')[-2]
dwn_url = 'https://drive.google.com/uc?export=download&id=' + file_id
url_content = requests.get(dwn_url).text
csv_raw = StringIO(url_content)
df_servidores = pd.read_csv(csv_raw, sep=';', decimal=',', thousands='.', low_memory=False)

#  desvio padrão dos salários líquidos para cada órgão
desvios_padrao = df_servidores.groupby('ÓRGÃO')['LÍQUIDO'].std()

# órgão com o menor desvio padrão menos variação
orgao_menos_variacao = desvios_padrao.idxmin()
menor_desvio_padrao = desvios_padrao.min()

print(f"O órgão com menos variação nos salários líquidos é '{orgao_menos_variacao}")
print(f"com um desvio padrão de {menor_desvio_padrao:.2f}.")


