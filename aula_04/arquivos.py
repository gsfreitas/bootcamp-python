import csv

path: str = "./files/products.csv"

csv_list: list = []

with open(file=path, mode="r", encoding="utf-8") as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        csv_list.append(row)
        print(row)