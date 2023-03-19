THIS IS SUPERPY!

Built with following modules:

Argparse, Pandas, Datetime, 

The command line commands written with Argparse module are the following arguments:
    
    show-date           Show system date
    set-current-date    Set system date to current date
    advance-date        Advance the date by a number of days
    register-purchase   Register sale of producth
    register-sale       Register the sale of a product
    show-total-revenue  Shows the total revenue
    show-date-revenue   Shows the total revenue, between two dates
    show-total-profit   Shows the total profit
    show-date-profit    Shows the total profit, between two dates
    show-inventory      Shows the currently available products, and gives the option to export as a .CSV file
    show-sales          Shows all the sales made
    show-purchases      Shows all the purchases made
    Help function

You can use the arguments as follow:

- python main.py show date  showing system date and saves it in date.txt

- python main.py set-current-date 
Using datetime module.

- python main.py advance-date --days 1
Jump with "1" day to new date.

- python main.py register-purchase --productname Beer --quantity 2 --price 2.00 --expiration 120
Register products bought with quantity, price and expiration due days.

- python main.py register-sale --productname Beer --quantity 1 --price 2.99
Register a sale of product by giving productname, quantity and price. (Reading data in sold.csv)

- python main.py show-total-revenue
Displays total sales.

- python main.py show-date-revenue --firstdate 2023-01-01 --seconddate 2023-03-03
Displays sales between two specific dates.

- python main.py show-total-profit
Displays total profit. Data from bought.csv and sold.csv

- python main.py show-date-profit --firstdate 2023-03-01 --seconddate 2023-03-17
Displays profit between two specific dates. 

- python main.py show-inventory
Displaying the products which are available

- python main.py show-inventory --exportCSV Yes
Displays and exports inventory to csv file

- python main.py show-sales
All sales read from sold.csv

- python main.py show-purchases
Displaying all purchases (Data read from bought.csv)




