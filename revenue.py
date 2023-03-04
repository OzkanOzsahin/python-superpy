
import inventory  
from rich import print

def get_total_revenue():
    sold_items = sold_items()
    total = 0
    for item in sold_items:
        total += float(item["sell_price"])
    return total


def print_total_revenue():
    total_revenue = get_total_revenue()
    print(f"Total revenue is: {total_revenue} eur")

def get_revenue_between_dates(first_date, second_date):
    total = 0
    items = items(first_date, second_date)
    for item in items:
        total += float(item["sell_price"])
    return total

def print_revenue_between_dates(first_date, second_date):
    revenue = get_revenue_between_dates(first_date, second_date)
    print(f"Total revenue in chosen period was {revenue} eur")