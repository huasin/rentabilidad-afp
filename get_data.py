import pandas as pd
import numpy as np

# Parametros
url = 'https://www.spensiones.cl/apps/rentabilidad/getRentabilidad.php?tiprent=FP'
nombre_fondo = list('ABCDE')
cn = ['afp','rentabilidad','acum_ano','acum_12_meses']

# Leer tablas
fondo = pd.read_html(url, header=1)
fondo = fondo[1:]

# Editar tablas
for i in range(5):
    fondo[i] = fondo[i].iloc[2:,:4]
    fondo[i].columns = cn
    fondo[i][['fondo']] = nombre_fondo[i]

# unimos los dfs
fondo = pd.concat(fondo)
fondo.index = np.arange(len(fondo))

# guardamos en la bd