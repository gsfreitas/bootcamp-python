import pandas as pd

df = pd.read_csv('./data/exemplo.csv')
df_filtrado = df[df['estado'] == 'SP']

print(df_filtrado)