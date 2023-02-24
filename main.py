#imports
import datetime
import csv
import os.path
import argparse
import pandas as pd





# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"

#Conception of what day it is
now = datetime.datetime.now()
today = now.strftime("%Y-%m-%d")
# Save the current date to a text file
with open("current_date.txt", "w") as f:
 f.write(today)

# Read the saved date from the text file
with open("current_date.txt", "r") as f:
    saved_date = f.read().strip()

# Check if the saved date matches the current date
if saved_date == today:
    print("Today is", today)
else:
    print("Today is today", today)
    



#create ArgumentParser object
parser = argparse.ArgumentParser(description='Process data')

#Add argument
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer to be processed')

# Your code below this line
def main():
    pass

#import and read csv



#pandas
df = pd.read_csv('bought.csv')
print(df)
        
# Add parsers


if __name__ == "__main__":
    main()