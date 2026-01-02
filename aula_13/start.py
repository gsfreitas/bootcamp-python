from fastapi import FastAPI
from faker import Faker
import pandas as pd
import random

app = FastAPI(debug=True)
fake = Faker()

file_path = "C:/Users/gfrei/Documents/3. PROJETOS/2. JORNADA_DE_DADOS/bootcamp_python/aula_13/data/products.csv"
df = pd.read_csv(file_path)
df['indice'] = range(1, len(df) + 1)
df = df.set_index('indice', inplace=True)

lojapadraoonline = 11

@app.get("/")
async def hello_world():
    return 'Hello, World!'

@app.get("/gerar_compra")
async def gerar_compra():
    index = random.randint(1, len(df)-1)
    tuple = df.iloc[index]

    return [{
        "client": fake.name(),
        "credit_card": fake.credit_card_provider(),
        "product": tuple["Product Name"],
        "ean": tuple["EAN"],
        "price": round(float(tuple["Price"])*1.2, 2),
        "clientPosition": fake.location_on_land(),
        "store": lojapadraoonline,
        "dateTime": fake.iso8601()
    }]

@app.get("/gerar_compras/{numero_registro}")
async def gerar_compras(numero_registro: int):

    if numero_registro < 1:
        return {"error": "O número de registros deve ser maior que 0"}

    respostas = []

    for _ in range(numero_registro):
        try:
            index = random.randint(1, len(df)-1)
            tuple = df.iloc[index]
            compra = {
                "client": fake.name(),
                "credit_card": fake.credit_card_provider(),
                "product": tuple["Product Name"],
                "ean": tuple["EAN"],
                "price": round(float(tuple["Price"])*1.2, 2),
                "clientPosition": fake.location_on_land(),
                "store": lojapadraoonline,
                "dateTime": fake.iso8601()
            }
            respostas.append(compra)
        except IndexError as e:
            print(f"Erro de indice: {e}")
        except ValueError as e:
            print(f"Erro de valor: {e}")
            compra = {
                "client": fake.name(),
                "credit_card": fake.credit_card_provider(),
                "product": "Produto não encontrado",
                "ean": "N/A",
                "price": 0.0,
                "clientPosition": fake.location_on_land(),
                "store": lojapadraoonline,
                "dateTime": fake.iso8601()
            }
            respostas.append(compra)
        except Exception as e:
            print(f"Erro geral: {e}")
    return respostas
    