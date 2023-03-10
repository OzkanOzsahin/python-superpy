
import argparse
import pandas as pd
from date import advance_time, print_date, set_current_date
from sales import sell_product
from inventory import export_inventory, display_sales, display_purchases
from revenue import print_revenue_between_dates, print_total_revenue
from profit import print_total_profit, print_profit_between_dates
from purchases import purchase_product


# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


#create ArgumentParser 
parser = argparse.ArgumentParser(description='Process data')

#Add parsers..

subparser = parser.add_subparsers(dest="command", required=True)
show_date = subparser.add_parser("show-date", help="Show system date")
set_today = subparser.add_parser("set-current-date", help="Set system date to current date")
advance_date = subparser.add_parser("advance-date", help="Advance the date by a number of days")
purchase = subparser.add_parser("register-purchase", help="Register sale of producth")
sale = subparser.add_parser("register-sale", help="Register the sale of a product")
total_revenue = subparser.add_parser("show-total-revenue", help="Shows the total revenue")
date_revenue = subparser.add_parser("show-date-revenue", help="Shows the total revenue, between two dates")
total_profit = subparser.add_parser("show-total-profit", help="Shows the total profit")
date_profit = subparser.add_parser("show-date-profit", help="Shows the total profit, between two dates")
inventory = subparser.add_parser("show-inventory", help="Shows the currently available products, and gives the option to export as CSV or PDF")
sales = subparser.add_parser("show-sales", help="Shows all the sales made")
purchases = subparser.add_parser("show-purchases", help="Shows all the purchases made")

advance_date.add_argument("--days", type=int)

purchase.add_argument("--productname", type = str)
purchase.add_argument("--quantity", type = int)
purchase.add_argument("--price", type = float)
purchase.add_argument("--expiration", type = int)

sale.add_argument("--productname", type= str)
sale.add_argument("--quantity", type= int)
sale.add_argument("--price", type= float)


date_revenue.add_argument("--firstdate", type= str)
date_revenue.add_argument("--seconddate", type= str)

date_profit.add_argument("--firstdate", type= str)
date_profit.add_argument("--seconddate", type= str)

inventory.add_argument("-c", "--exportCSV", type= str)
inventory.add_argument("-p", "--exportPDF", type= str)

args = parser.parse_args()
if args.command == "show-date":
    show_date.set_defaults(
        func=print_date()
    )

if args.command == "set-current-date":
    show_date.set_defaults(
        func= set_current_date()
    )

if args.command == "advance-date":
    advance_date.set_defaults(
        func=advance_time(args.days)
    )

if args.command == "register-purchase":
    purchase.set_defaults(
        func = purchase_product(
            args.productname, 
            args.quantity,
            args.price,
            args.expiration
        )
    )

if args.command == "register-sale":
    sale.set_defaults(
        func=sell_product(
            args.productname,
            args.quantity,
            args.price
        )
    )

if args.command == "show-total-revenue":
    total_revenue.set_defaults(func=print_total_revenue)
    

if args.command == "show-date-revenue":
    date_revenue.set_defaults(
        func=print_revenue_between_dates(
            args.firstdate,
            args.seconddate
        )
    )

if args.command == "show-total-profit":
    total_profit.set_defaults(
        func=print_total_profit()
    )

if args.command == "show-date-profit":
    date_profit.set_defaults(
        func=print_profit_between_dates(
            args.firstdate,
            args.seconddate
        )
    )

if args.command == "show-inventory":
    inventory.set_defaults(func=export_inventory(
        args.exportCSV,
        args.exportPDF,
    ))


if args.command == "show-sales":
    sales.set_defaults(
        func=display_sales()
    )

if args.command == "show-purchases":
    purchases.set_defaults(
        func=display_purchases()
    )


# Your code below this line


#import and read csv



#pandas
df = pd.read_csv('bought.csv')
print(df)
