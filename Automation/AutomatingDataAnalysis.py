#  Este codigo fue extraido desde la siguiente pagina
#  https://medium.com/@naseer1015922/5-killer-python-scripts-for-automation-part1-e83383740154
#  Fue creado por https://medium.com/@naseer1015922

import pandas as pd

# Reading a CSV file
df = pd.read_csv("data.csv")

# Cleaning data
df.dropna(inplace=True) # Dropping missing values
df = df[df["column_name"] != "some_value"] # Removing specific rows

# Transforming data
df["column_name"] = df["column_name"].str.lower() # Changing string to lowercase
df["column_name"] = df["column_name"].astype(int) # Changing column datatype

# Analyzing data
print(df["column_name"].value_counts()) # Prints the frequency of unique values in the column

# Saving the cleaned and transformed data to a new CSV file
df.to_csv("cleaned_data.csv", index=False)
