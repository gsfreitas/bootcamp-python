from interface.classes.csv_class import CSVProcessor

path = './exemplo.csv'
filter_column = 'estado'
limit = 'SP'

csv_file = CSVProcessor(path)
# csv_file.carregar_csv()
csv_file.filter(filter_column, limit)

print("#"*20)

print(csv_file.filter(filter_column, limit))
print(csv_file.sub_filter('preco', 110.20))