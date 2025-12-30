from src.interface.classes.exemplo_csv_class import CsvProcessor

arquivo_csv = './data/exemplo.csv'
filtro = 'estado'
limite = 'SP'

arquivo_CSV = CsvProcessor(arquivo_csv)
arquivo_CSV.carregar_csv()
print('filtro1')
print(arquivo_CSV.filtrar_por('preco', 100))
print('filtro2')
print(arquivo_CSV.sub_filtro(filtro, limite))
print('df')
print(arquivo_CSV.df)