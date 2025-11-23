from interface.classes.csv_class import CSVProcessor

path = './source/data/exemplo.csv'

csv_file = CSVProcessor(path)

print("#"*20)

print(csv_file.filter(['estado', 'preco'], ['SP', 110.20]))