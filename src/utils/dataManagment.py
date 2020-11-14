import pandas as pd
from sodapy import Socrata
import dateutil
from datetime import datetime


client = Socrata("www.datos.gov.co", None)
results = client.get("gt2j-8ykr", limit=1000)

df = pd.DataFrame.from_records(results)
df['fecha_de_notificaci_n'] = df['fecha_de_notificaci_n'].apply(dateutil.parser.parse,dayfirst=True)
print(df)

def data_frame_head(number):
    num = int(number)
    return df.head(num)

def get_sex_country_deaths(country,sex):
    data = df[(df['sexo'] == sex) & (df['pais_viajo_1_nom'] == country) & (df['recuperado'] == 'Fallecido')]
    return data

def get_country_dates(country,firstDate,secondDate):
    print("Pandas: "  + str(firstDate))
    print("Pandas: "  + str(secondDate))
    data = df[(df['pais_viajo_1_nom'] == country) & (df['fecha_de_notificaci_n'] >= firstDate) & (df['fecha_de_notificaci_n'] <= secondDate) 
    & (df['recuperado'] == 'Fallecido')]
    return data