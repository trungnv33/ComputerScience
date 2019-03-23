import pandas as pd
df= pd.read_excel('titanic.xls')
print(df.columns.values)
print(df['name'])
df_val = list(set(df['name']))
print((df_val))