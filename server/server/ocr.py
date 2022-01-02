import pytesseract as tess
from PIL import Image
import re
from models.product import Product

def img_to_bill(img_path: str):
    img = Image.open(img_path)
    text = tess.image_to_string(img)
    text = text[text.find('Lei\n') + 4:text.find("\nSUBTOTAL")]
    text = text.split("\n")
    products = []
    i = 0
    while i < len(text):
        line = text[i]
        line = line.replace(',', '.')
        quantity, price = line.split("x")
        is_countable = False
        if 'BUC' in quantity:
            is_countable = True
            quantity = float(re.split(r"\.", quantity)[0])
        else:
            quantity = float(re.split(r'\s', quantity)[0])
        price = float(price)
        name = re.split(r'\d+[\.,]\d*', text[i + 1])[0]
        print(name, price ,quantity, is_countable)
        products.append(Product(name, price, quantity, is_countable))

        i += 2
    
    print(products)

img_to_bill("../test.png")