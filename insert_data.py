import pandas as pd
import sqlite3
import feather
import os

conn = sqlite3.connect('db')
file_names = os.listdir('files/')
file_paths = ['files/' + fn for fn in file_names]

for fp in file_paths:
    df = feather.read_dataframe(file_path)
    df.to_sql(name = 'rentabilidad_afp', con = conn, if_exists = 'append', index = False)

query = "select fecha, count(*) from rentabilidad_afp group by fecha order by fecha"
df = pd.read_sql(query, con = conn)

conn.close()