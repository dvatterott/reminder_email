"""Send an email when needed."""
from datetime import datetime as dt
from os import system
from os import path

str_format = '%Y-%m-%d'
file_path = "/home/fake_user/reminder_email/dates.txt"

if __name__ == "__main__":
    if path.isfile(file_path):
        with open(file_path) as f:
            dates = f.readlines()
    dates = [x.rstrip('\n') for x in dates]
    
    if any([x == dt.today().strftime(str_format) for x in dates]):
        system("""echo Do X | mail -s "Reminder" -a "From: Dan <dan@example.com>" fake_addy@gmail.com""")
    
