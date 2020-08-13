import pandas as pd
import numpy as np
import datetime
from selenium import webdriver
from read_page import get_afp_page, get_afp_data
import feather
import time
# from selenium.webdriver.common.keys import Keys

month_names = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
PATH = '/home/huasin/chromedriver'
driver = webdriver.Chrome(PATH)
url = 'https://www.spensiones.cl/apps/rentabilidad/getRentabilidad.php?tiprent=FP&template=0'
driver.get(url)

years  = np.arange(2005,2021).tolist()
months = np.arange(1,13).tolist()
tuples = [(year,month) for year in years for month in months]

# year = 2020
# month = 1

for year, month in tuples:

    # Casos que no caben
    if year == 2005 and month <= 7:
        continue
    elif year == 2020 and month >= 8:
        continue

    month_name = month_names[month-1]

    # Scrapeamos la data
    page = get_afp_page(driver,year,month_name)
    df = get_afp_data(page)

    # Agrego la fecha
    df[['fecha']] = datetime.date(year,month,1)

    # Elimino % y coma por punto
    df.iloc[:,1:4] = df.iloc[:,1:4].apply(lambda x: x.str.replace('%',''))
    df.iloc[:,1:4] = df.iloc[:,1:4].apply(lambda x: x.str.replace(',','.'))

    # Conversion de tipos
    df = df.astype('string')
    df.iloc[:,1:4] = df.iloc[:,1:4].apply(lambda x: pd.to_numeric(x, errors='coerce')/100)
    df['fecha'] = pd.to_datetime(df['fecha'], format='%Y-%m-%d')

    # Creamos nombre y guardamos
    save = 'files/rentabilidad_afp_'+str(year)+'{:0>2}'.format(month)+'.feather'
    feather.write_dataframe(df,save)

    time.sleep(5)
    
# Se cierra el browser
driver.quit()
