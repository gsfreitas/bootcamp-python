import pandas as pd

class CSVProcessor:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.df = pd.read_csv(self.file_path)

    def filter(self, columns, attributes, df=None):
        # A primeira chamada usa o dataframe original
        if df is None:
            df = self.df

        if len(columns) != len(attributes):
            raise ValueError("O número de colunas e atributos deve ser igual.")

        # Caso base: nenhum filtro → retorne o df atual
        if len(columns) == 0:
            return df

        current_column = columns[0]
        current_attribute = attributes[0]

        # Filtra com base no dataframe recebido
        df_filtered = df[df[current_column] == current_attribute]

        # Caso base final
        if len(columns) == 1:
            return df_filtered

        # Chamada recursiva com o dataframe já filtrado
        return self.filter(columns[1:], attributes[1:], df_filtered)
