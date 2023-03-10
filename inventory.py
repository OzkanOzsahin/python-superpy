import pandas as pd
import csv
import os.path
from date import get_date
from rich.table import Table
from fpdf import FPDF
from rich.console import Console



bought_path = "./bought.csv"
sold_path = "./sold.csv"
transactions_path = "./transactions.csv"
console = Console()

 

def get_bought_items():
    bought_items = []
    with open(bought_path, "r", encoding="utf-8-sig") as bought_object:
        reader = csv.DictReader(bought_object)
        for row in reader:
            bought_items.append(row)
    return bought_items

def get_sold_ids():
    sold_ids = []
    with open(sold_path, "r", encoding="utf-8-sig") as sold_object:
        reader = csv.DictReader(sold_object)
        for row in reader:
            sold_ids.append(row["bought_id"])
    return sold_ids

def get_sold_items():
    sold_items = []
    with open(sold_path, "r", encoding="utf-8-sig") as sold_object:
        reader = csv.DictReader(sold_object)
        for row in reader:
            sold_items.append(row)
    return sold_items

def get_available_products():
    bought_items = get_bought_items()
    sold_ids = get_sold_ids()
    available_products = []
    today = get_date()
    for item in bought_items:
        if item["id"] not in sold_ids and item["expiration_date"] >= today:
            available_products.append(item)
    return available_products

def get_expired_products():
    bought_items = get_bought_items()
    sold_ids = get_sold_ids()
    expired_products = []
    today = get_date()
    for item in bought_items:
        if item["id"] not in sold_ids and item["expiration_date"] < today:
            expired_products.append(item)
    return expired_products

def get_available_product(product_name):
    bought_items = get_bought_items()
    sold_ids = get_sold_ids()
    availabe_products = []
    today = get_date()
    for item in bought_items:
        if item['id'] not in sold_ids and item['expiration_date'] >= today and item['product_name'] == product_name:
            availabe_products.append(item)
    if availabe_products == []:
        print('Sorry, no available products were found.')
    else:
        return availabe_products

def get_sold_between_dates(first_date, second_date):
    sold_items = get_sold_items()
    items = []
    for item in sold_items:
        if item["sell_date"] >= first_date and item["sell_date"] <= second_date:
            items.append(item)
    return items

def get_bought_between_dates(first_date, second_date):
    bought_items = get_bought_items()
    items = []
    for item in bought_items:
        if item["buy_date"] >= first_date and item["buy_date"] <= second_date:
            items.append(item)
    return items

def get_inventory():
    items = get_available_products()
    inventory = {}
    for item in items:
        if item['product_name'] in inventory.keys():
            inventory[item['product_name']] += 1
        else:
            inventory.update({item['product_name']: 1})
    return inventory

def display_inventory():
    inventory = get_inventory()
    table = Table(show_header=True, header_style="bold green")
    table.add_column('Product', style='dim', width=12)
    table.add_column('Current stock')
    for key, value in inventory.items():
        table.add_row(
            key,
            str(value),
        )
    console.print(table)

def display_sales():
    sales = get_sold_items()
    purchases = get_bought_items()
    for item in sales:
        for product in purchases:
            if item['bought_id'] == product['id']:
                item.update({'product_name': product['product_name']})
    table = Table(show_header=True, header_style="bold green")
    table.add_column('Product', style='dim', width=12)
    table.add_column('Date of sale')
    table.add_column('Price')
    for item in sales:
        table.add_row(
            item['product_name'],
            item['sell_date'],
            item['sell_price']
        )
    console.print(table)

def display_purchases():
    purchases = get_bought_items()
    table = Table(show_header=True, header_style="bold green")
    table.add_column('Product', style='dim', width=12)
    table.add_column('Date of purchase')
    table.add_column('Price')
    table.add_column('Expiration date')
    for item in purchases:
        table.add_row(
            item['product_name'],
            item['buy_date'],
            item['buy_price'],
            item['expiration_date']
        )
    console.print(table)

def export_inventory(export_csv, export_pdf):
    inventory = get_inventory()
    export_csv = "./export_inventory.csv"
    path_pdf = "./export_inventory.pdf"
    if export_csv == "Yes":
        if os.path.isfile(export_csv):
            print(f"This file already exists")
        else:
            with open(export_csv, "w", newline ="") as file:
                csv_writer = csv.writer(file)
                for product, quantity in inventory.items():
                    products = [product, quantity]
                    csv_writer.writerow(products)
            display_inventory()
            print(f"CSV file created")
    elif export_pdf == "Yes":
        if os.path.isfile(path_pdf):
            print(f"This file already exists")
        else:
            with open(export_csv, newline= "") as file:
                reader = csv.reader(file)
                
                pdf = FPDF()
                pdf.add_page()
                page_width = pdf.w - 2 * pdf.l_margin
                    
                pdf.set_font('Times','B',14.0) 
                pdf.cell(page_width, 0.0, 'Inventory', align='C')
                pdf.ln(10)

                pdf.set_font('Courier', '', 12)
                
                col_width = page_width/4
                
                pdf.ln(1)
                
                th = pdf.font_size
                
                for row in reader:
                    pdf.cell(col_width, th, str(row[0]), border=1)
                    pdf.cell(col_width, th, row[1], border=1)
                    pdf.ln(th)
                    
                pdf.ln(10)

                pdf.set_font('Times','',10.0) 
                pdf.cell(page_width, 0.0, '- end of report -', align='C')
                
                pdf.output(path_pdf, 'F')
            display_inventory()
            print(f"PDF file created")
    else:
        display_inventory()





