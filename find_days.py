"""Find dates to send reminder email."""
from datetime import datetime as dt
from datetime import timedelta as td
from random import randint
from os import path

str_format = '%Y-%m-%d'
file_path = "/home/fake_user/article_reminder/dates.txt"

if __name__ == "__main__":
    year, month, _ = dt.today().strftime(str_format).split('-')
    current_day = int(dt.today().strftime('%u'))
    
    if path.isfile(file_path):
        with open(file_path) as f:
            dates = f.readlines()
        if len(dates) > 0:
            final_date = dt.strptime(dates[-1].rstrip('\n'), str_format)
        else:
            final_date = dt.strptime('1987-06-16', str_format)
    else:
        final_date = dt.strptime('1987-06-16', str_format)

    if (not path.isfile(file_path)) or ((dt.today() - td(days=int(dt.today().strftime('%u')))) > final_date): 
        next_email = dt.today() + td(days=randint(0, 7-current_day))
        print next_email.strftime(str_format)

    next_sunday = dt.today() + td(days=7-current_day)

    while (int(next_sunday.strftime('%m')) <= int(month)) and (int(next_sunday.strftime('%Y')) <= int(year)):
       try_day = next_sunday + td(days=randint(0,6))
       print try_day.strftime(str_format)
       next_sunday = next_sunday + td(days=7)
