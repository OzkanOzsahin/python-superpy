#imports

import csv
import os






# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"



# Your code below this line
def main():
    pass

#import and read csv

    filepath = os.path.join(os.getcwd(), "inventory.csv")
    with open(filepath, 'r', newline='') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            inventory_list = list(csv_reader)

    for row in csvfile:
         print(row)


# Add parsers
