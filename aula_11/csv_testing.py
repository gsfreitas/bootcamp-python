import pandas as pd

df = pd.read_csv('./exemplo.csv')

df_filtered = df[df['estado'] == 'SP']

print(df_filtered)