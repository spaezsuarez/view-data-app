import pandas as pd
from sodapy import Socrata


def init_data_frame():
    client = Socrata("www.datos.gov.co", None)
    results = client.get("gt2j-8ykr", limit=1000)

    df = pd.DataFrame.from_records(results)
    return df

