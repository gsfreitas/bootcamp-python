from faker import Faker
import pandas as pd
import random

fake = Faker()

# Generate 500 products
products = []
for i in range(500):
    # EAN-13 barcode (13 digits)
    ean = ''.join([str(random.randint(0, 9)) for _ in range(13)])
    
    # Product name
    product_name = fake.catch_phrase() + " " + fake.word().title()
    
    # Price (between 5.00 and 999.99)
    price = round(random.uniform(5.00, 999.99), 2)
    
    products.append({
        'EAN': ean,
        'Product Name': product_name,
        'Price': price
    })

# Create DataFrame
df = pd.DataFrame(products)

# Save to CSV
df.to_csv('products.csv', index=False)
print(f"CSV file 'products.csv' created successfully with {len(products)} products!")

