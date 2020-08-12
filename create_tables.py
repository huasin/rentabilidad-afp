import sqlite3

# Creo conexion
conn = sqlite3.connect('db')

# Abro cursor
cursor = conn.cursor()

query = """
    CREATE TABLE IF NOT EXISTS rentabilidad_afp(
        afp VARCHAR(16) NOT NULL,
        rentabilidad FLOAT,
        acum_ano FLOAT,
        acum_12_meses,
        fondo VARCHAR(1),
        fecha DATE NOT NULL
    )
"""

cursor.execute(query)

# Cierro cursor
cursor.close()

# Guardo los datos
conn.commit()

# Cierro conexion
conn.close()