REPORT

This is a short report on my Superpy project.  It involves an explanation of which modules i have used and some examples of my code i have written. Hopefully i used it all in the right way.

PANDAS (python library)

It was hard to find the write way to easily read external files (csv) and display them in the command- line - interface, storing and writing data to my csv file again. So at last i used Pandas. In my main.py file you will see my import code. 

DATE

I have created a function to print and show current date and time. 
For imports and codes you can follow my date.py


INVENTORY
A function(code) that shows products in store; products/goods bought, sold and an opportunity
to display inventory in csv or pdf file.

For an example: 
def export_inventory(export_csv, export_pdf):
    inventory = get_inventory()
    
    if export_csv:
        if os.path.isfile(export_csv):
            print(f"The CSV file '{export_csv}' already exists")
        else:
            with open(export_csv, "w", newline="") as file:
                csv_writer = csv.writer(file)
                for product, quantity in inventory.items():
                    products = [product, quantity]
                    csv_writer.writerow(products)
            print(f"CSV file '{export_csv}' created")


PROFIT 

A file and possibilities displaying profits made in a specific period.

def get_total_profit():
    bought_items = get_bought_items()
    total_revenue = get_total_revenue()
    total = 0 
    for item in bought_items:
        total += float(item["buy_price"])

    sum = total_revenue - total
    return sum

PURCHASES

Shows purchases have been made. And gives you the
possibility to register purchases.

def purchase_product(product_name, quantity, price, expiration_days):
    today = get_date()
    expiration = get_expiration_date(expiration_days)
    path = "bought.csv"
    with open(path, "a", newline ="") as file:
        csv_writer = csv.writer(file)
        for i in range(quantity):
            id = get_new_id(path) + i
            product = [id, product_name, today, price, expiration]
            csv_writer.writerow(product)
    print(f"You have purchased {quantity}x {product_name}, costing {price} eur per piece, they will expire on {expiration}")

REVENUE

Shows revenue the superpy has made

def get_total_revenue():
    sold_items = get_sold_items()
    total = 0
    for item in sold_items:
        total += float(item["sell_price"])
    return total

SALES

Shows sales the superpy has made. Also gives you the possibility to register sales.
Here there should be an automatic upload to bought.csv









