import pandas as pd
import csv


def add_product(boughts):
    """Add a new product to the inventory."""
    print("Enter the product details:")
    product_name = input("Name: ")
    product_type = input("Type: ")
    product_quantity = int(input("Quantity: "))
    product_cost = float(input("Cost: "))
    product_expiry = input("Expiry date (YYYY-MM-DD): ")
    with open(boughts, mode='a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([product_name, product_type, product_quantity,
                         product_cost, product_expiry])
    print("Product added successfully.")

def update_product(products_file):
    """Update an existing product in the inventory."""
    product_name = input("Enter the name of the product to update: ")
    found = False
    with open(products_file, mode='r') as csv_file:
        reader = csv.reader(csv_file)
        rows = []
        for row in reader:
            if row[0] == product_name:
                found = True
                print("Current details:")
                print(f"Type: {row[1]}, Quantity: {row[2]}, Cost: {row[3]}, Expiry: {row[4]}")
                new_type = input("New type (leave blank to keep current value): ")
                new_quantity = input("New quantity (leave blank to keep current value): ")
                new_cost = input("New cost (leave blank to keep current value): ")
                new_expiry = input("New expiry date (leave blank to keep current value): ")
                if new_type == "":
                    new_type = row[1]
                if new_quantity == "":
                    new_quantity = row[2]
                else:
                    new_quantity = int(new_quantity)
                if new_cost == "":
                    new_cost = row[3]
                else:
                    new_cost = float(new_cost)
                if new_expiry == "":
                    new_expiry = row[4]
                rows.append([product_name, new_type, new_quantity, new_cost, new_expiry])
            else:
                rows.append(row)
    if not found:
        print("Product not found.")
        return
    with open(products_file, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(rows)
    print("Product updated successfully.")

def remove_product(products_file):
    """Remove a product from the inventory."""
    product_name = input("Enter the name of the product to remove: ")
    found = False
    with open(products_file, mode='r') as csv_file:
        reader = csv.reader(csv_file)
        rows = []
        for row in reader:
            if row[0] == product_name:
                found = True
            else:
                rows.append(row)
    if not found:
        print("Product not found.")
        return
    with open(products_file, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(rows)
    print("Product removed successfully.")

def list_products(products_file):
    """List all products in the inventory."""
    with open(products_file, mode='r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            print(f"{row[0]} ({row[1]}), Quantity: {row[2]}, Cost: {row[3]}, Expiry: {row[4]}")

def add_sale(sales_file, products_file):
    """Add a new sale to the records."""
    print("Enter the sale")





