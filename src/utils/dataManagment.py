import pandas as pd
from sodapy import Socrata

client = Socrata("www.datos.gov.co", None)
results = client.get("gt2j-8ykr", limit = 10000)

df = pd.DataFrame.from_records(results)
df['fecha_inicio_sintomas'] = pd.to_datetime(df['fecha_inicio_sintomas'], format='%d/%m/%Y %H:%M:%S').dt.date

def data_frame_head(number):
    num = int(number)
    return df.head(num)

def get_sex_country_deaths(country,sex):
    data = df[(df['sexo'] == sex) & (df['pais_viajo_1_nom'] == country) & (df['recuperado'] == 'Fallecido')]
    return data

def get_country_dates(country,firstDate,secondDate):

    data = df[(df['pais_viajo_1_nom'] == country) & (df['fecha_inicio_sintomas'] >= firstDate) & (df['fecha_inicio_sintomas'] <= secondDate)]
    return data

def get_contagios_por_pais(sexo):
    data = df['pais_viajo_1_nom'][df['sexo'] ==sexo].value_counts()
    return data.to_frame()
