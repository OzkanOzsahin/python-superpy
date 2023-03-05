import datetime
path = "./date.txt"
now = datetime.datetime.now()
print("Current date and time")
print(now)

def get_date():
    with open(path, "r") as file:
        for line in file:
            return line
        
def print_date():
    date = ""
    with open(path, "r") as file:
        for line in file:
            date = line
    print(f"Show current date: {date}")

def set_current_date():
    today = str(datetime.date.today())
    with open(path, "w") as file:
        file.write(today)
    print(f"Date has changed to: {today}")

def advance_time(days):
    today = datetime.datetime.strptime(get_date(), "%Y-%m-%d") .date()
    new_date = today + datetime.timedelta(days)
    with open(path, "w") as file:
        file.write(str(new_date))
        print(f"New date is: {new_date}")
        
         


