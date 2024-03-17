import requests
from io import StringIO
import pandas as pd

# URL do arquivo CSV
orig_url = 'https://drive.google.com/file/d/1UrlwBHa47H5lpAkLtDsfuEWfTMQj491X/view?usp=sharing'

# Extraindo o ID do arquivo da URL
file_id = orig_url.split('/')[-2]

# Construindo URL de download 
dwn_url = 'https://drive.google.com/uc?export=download&id=' + file_id

# Obtendo o conteúdo do arquivo CSV como texto
url_content = requests.get(dwn_url).text

# Convertendo o texto em um objeto StringIO
csv_raw = StringIO(url_content)

# Lendo conteúdo do arquivo CSV com o pandas
df_servidores = pd.read_csv(csv_raw, sep=';', low_memory=False)

# Determinando o tamanho do espaço amostral (número de linhas)
espaco_amostral = len(df_servidores)

print("O espaço amostral compreendido nesta base de dados é de", espaco_amostral, "observações.")