from datetime import datetime
import csv

#creating a list to hold transactions
transactions = []

#Creating a function to record a transaction
def record_transaction(action, product, quantity, price):
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    transactions.append([date_time, action, product, quantity, price])


#record a transaction 
record_transaction("buy", "apple", 10, 0.5)

# Record a transaction for selling a product
record_transaction("sell", "apple", 5, 0.7)

# Write the transactions to a CSV file
with open('transactions.csv', mode='w') as file:
    writer = csv.writer(file)
    writer.writerow(["Date", "Action", "Product", "Quantity", "Price"])
    for transaction in transactions:
        writer.writerow(transaction)