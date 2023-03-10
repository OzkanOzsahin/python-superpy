from date import get_date
import csv
import datetime
from rich import print

def get_new_id(file):
    with open(file) as f:
        reader = csv.reader(f)
        new_id = len(next(zip(*reader)))
    return new_id
    
def get_expiration_date(days):
    date = get_date()
    today = datetime.datetime.strptime(date, "%Y-%m-%d"). date()
    new_date = today + datetime.timedelta(days=days)
    return new_date

def purchase_product(product_name, quantity, price, expiration_days):
    today = get_date()
    expiration = get_expiration_date(expiration_days)
    path = "./bought.csv"
    with open(path, "a", newline ="") as file:
        csv_writer = csv.writer(file)
        for i in range(quantity):
            id = get_new_id(path) + i
            product = [id, product_name, today, price, expiration]
            csv_writer.writerow(product)
    print(f"You have purchased {quantity}x {product_name}, costing {price} eur per piece, they will expire on {expiration}")