import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

# Parametros
url = 'https://www.spensiones.cl/apps/rentabilidad/getRentabilidad.php?tiprent=FP'
nombre_fondo = list('ABCDE')
cn = ['afp','rentabilidad','acum_ano','acum_12_meses']

# Scrap
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
tables = soup.find_all('table')
