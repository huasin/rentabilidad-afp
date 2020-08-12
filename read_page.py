import pandas as pd
import numpy as np

def get_afp_data(page):
    # Parametros
    nombre_fondo = list('ABCDE')
    cn = ['afp','rentabilidad','acum_ano','acum_12_meses']

    # Leer tablas
    fondo = pd.read_html(page, header=1)
    fondo = fondo[1:]

    # Editar tablas
    for i in range(5):
        fondo[i] = fondo[i].iloc[2:,:4]
        fondo[i].columns = cn
        fondo[i][['fondo']] = nombre_fondo[i]

    # unimos los dfs
    fondo = pd.concat(fondo)
    fondo.index = np.arange(len(fondo))

    return(fondo)

def get_afp_page(driver,year,month_name):

    select_year = driver.find_element_by_name('aaaa')
    select_month = driver.find_element_by_name('mm')
    btn_search = driver.find_element_by_name('btn')

    select_year.send_keys(year)
    select_month.send_keys(month_name)
    btn_search.click()

    # obtenemos el resultado
    page = driver.page_source
    return(page)