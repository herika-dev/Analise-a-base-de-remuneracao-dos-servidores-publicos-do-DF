import requests
import pandas as pd


orig_url = 'https://drive.google.com/file/d/1UrlwBHa47H5lpAkLtDsfuEWfTMQj491X/view?usp=sharing'
file_id = orig_url.split('/')[-2]
dwn_url = 'https://drive.google.com/uc?export=download&id=' + file_id
df_servidores = pd.read_csv(dwn_url, sep=';', decimal=',', thousands='.', low_memory=False)

# Convertendo as colunas LÍQUIDO,BRUTO e IRRF para float
df_servidores['LÍQUIDO'] = df_servidores['LÍQUIDO'].astype(float)
df_servidores['BRUTO'] = df_servidores['BRUTO'].astype(float)
df_servidores['IRRF'] = df_servidores['IRRF'].astype(float)

# Calculando a correlação entre IRRF e salário líquido e bruto
correlacao_irrf_liquido = df_servidores['IRRF'].corr(df_servidores['LÍQUIDO'])
correlacao_irrf_bruto = df_servidores['IRRF'].corr(df_servidores['BRUTO'])
#resultado 
print("Índice de correlação entre IRRF e salário líquido:", correlacao_irrf_liquido)
print("Índice de correlação entre IRRF e salário bruto:", correlacao_irrf_bruto)

if correlacao_irrf_liquido > correlacao_irrf_bruto:
    print("O índice de correlação foi maior entre IRRF e salário líquido.")
elif correlacao_irrf_liquido < correlacao_irrf_bruto:
    print("O índice de correlação foi maior entre IRRF e salário bruto.")
else:
    print("O índice de correlação foi igual nos dois casos.")