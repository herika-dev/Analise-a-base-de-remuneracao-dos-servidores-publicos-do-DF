import requests
from io import StringIO
import pandas as pd

orig_url = 'https://drive.google.com/file/d/1UrlwBHa47H5lpAkLtDsfuEWfTMQj491X/view?usp=sharing'
file_id = orig_url.split('/')[-2]
dwn_url = 'https://drive.google.com/uc?export=download&id=' + file_id
url_content = requests.get(dwn_url).text
csv_raw = StringIO(url_content)
df_servidores = pd.read_csv(csv_raw, sep=';', low_memory=False)

# Convertendo para numérico
df_servidores['BRUTO'] = pd.to_numeric(df_servidores['BRUTO'].str.replace(',', '.'), errors='coerce')

# Valor total pago a todos os funcionários públicos
total_pago = df_servidores['BRUTO'].sum()

# Formatando o valor para reais
total_pago_formatado = "{:,.2f}".format(total_pago).replace(",", ";").replace(".", ",").replace(";", ".")

print(f"O valor total pago a todos os funcionários públicos é de R$ {total_pago_formatado}")