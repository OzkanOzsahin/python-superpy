#imports

import os
import csv


# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"



# Your code below this line
def main():
    pass


#Importing and reading the csv files
with open('bought.csv', 'r') as file:
  csvreader = csv.reader(file)
  for row in csvreader:
    print(row)
