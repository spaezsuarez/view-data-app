import pandas as pd
import numpy as np
from sodapy import Socrata

client = Socrata("www.datos.gov.co", None)
results = client.get("gt2j-8ykr", limit=10000)

df = pd.DataFrame.from_records(results)
df['fecha_inicio_sintomas'] = pd.to_datetime(df['fecha_inicio_sintomas'], format='%d/%m/%Y %H:%M:%S').dt.date


def test():
    return df.groupby('ciudad_municipio_nom').count()

def data_frame_head(number):
    num = int(number)
    return df.head(num)


def get_sex_country_deaths(country, sex):
    data = df[(df['sexo'] == sex) & (df['pais_viajo_1_nom'] ==
                                     country) & (df['recuperado'] == 'Fallecido')]
    return data


def get_country_dates(country, firstDate, secondDate):
    data = df[(df['pais_viajo_1_nom'] == country) & (df['fecha_inicio_sintomas']
                                                     >= firstDate) & (df['fecha_inicio_sintomas'] <= secondDate)]
    return data


def get_contagios_por_pais(sexo):
    data = df['pais_viajo_1_nom'][df['sexo'] == sexo].value_counts()
    return data.to_frame()


def get_estado_por_pais(estado):
    data = df[df['recuperado'] == estado]
    DataGroupBy = data.groupby(['departamento_nom'])['recuperado'].count()
    return DataGroupBy.to_frame()
    

def get_resumen(departamento):
    data = df[(df['departamento_nom'] == departamento) & (df['recuperado'] == 'Fallecido')]
    data = data.loc[:,['edad','per_etn_']]
    data_group = data.agg(['mean',np.median,'max'])
    return data_group

def get_muertes_por_ciudad(city):
    data = df[(df['recuperado'] == 'Fallecido') & (df['ciudad_municipio_nom'] == city)]
    data_group = data.groupby(['ciudad_municipio_nom'])['id_de_caso'].count()
    result = data_group.to_frame()
    return result