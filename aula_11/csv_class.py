import pandas as pd

class CSVProcessor:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.df = None
        self.df = pd.read_csv(self.file_path)

    def filter(self, column, attribute):
        return self.df[self.df[column] == attribute]

path = './exemplo.csv'
filter_column = 'estado'
limit = 'SP'

csv_file = CSVProcessor(path)
# csv_file.carregar_csv()
print(csv_file.filter(filter_column, limit))