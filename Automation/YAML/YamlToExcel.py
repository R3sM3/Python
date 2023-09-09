import yaml
import pandas as pd

# Lee el archivo YAML
with open('example.yaml', 'r') as yaml_file:
    data = yaml.load(yaml_file, Loader=yaml.FullLoader)

# Define una función para eliminar registros específicos
def eliminar_registros(data, eliminar_estos):
    for registro in eliminar_estos:
        if registro in data:
            del data[registro]

# Llama a la función para eliminar registros específicos
registros_a_eliminar = ["registro1", "registro2"]  # Reemplaza con los registros que deseas eliminar
eliminar_registros(data, registros_a_eliminar)

# Convierte los datos en un DataFrame de pandas
df = pd.DataFrame.from_dict(data)

# Guarda el DataFrame en un archivo Excel
with pd.ExcelWriter('resultado.xlsx', engine='openpyxl') as writer:
    df.to_excel(writer, sheet_name='Hoja1', index=False)

print("Registros eliminados y el resultado se ha guardado en 'resultado.xlsx'.")
