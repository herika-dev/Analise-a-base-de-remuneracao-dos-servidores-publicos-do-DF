import requests
from io import StringIO
import pandas as pd

orig_url = 'https://drive.google.com/file/d/1UrlwBHa47H5lpAkLtDsfuEWfTMQj491X/view?usp=sharing'
file_id = orig_url.split('/')[-2] 
dwn_url = 'https://drive.google.com/uc?export=download&id=' + file_id
url_content = requests.get(dwn_url).text
csv_raw = StringIO(url_content)
df_servidores = pd.read_csv(csv_raw, sep=';', low_memory=False)

# Convertendo colunas para numérico
df_servidores['BRUTO'] = pd.to_numeric(df_servidores['BRUTO'].str.replace(',', '.'), errors='coerce')
df_servidores['LÍQUIDO'] = pd.to_numeric(df_servidores['LÍQUIDO'].str.replace(',', '.'), errors='coerce')
df_servidores['IRRF'] = pd.to_numeric(df_servidores['IRRF'].str.replace(',', '.'), errors='coerce')

# Adicionando uma nova coluna com a diferença entre salário bruto e líquido
df_servidores['Diferenca_Salario'] = df_servidores['BRUTO'] - df_servidores['LÍQUIDO']

#  correlação entre as colunas IRRF e 'Diferenca_Salario'
corr_irrf_dif_sal = df_servidores['IRRF'].corr(df_servidores['Diferenca_Salario'])

print(f"A correlação entre IRRF e a nova coluna Diferenca_Salario é de: {corr_irrf_dif_sal:.3f}")

# correlação por órgão
orgao_correlacao = df_servidores.groupby('ÓRGÃO')[['IRRF', 'Diferenca_Salario']].corr().iloc[0::2, -1]

# órgão com a maior correlação
orgao_maior_corr = orgao_correlacao.idxmax()

#  valor da maior correlação
maior_correlacao = orgao_correlacao.max()

print(f"O órgão que apresenta índice de correlação entre IRRF e Diferenca_Salario maior é '{orgao_maior_corr}'.")
print(f"com um índice de correlação de {maior_correlacao:.2f}.")