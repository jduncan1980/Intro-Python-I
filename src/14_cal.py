"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

    
import sys
import calendar
from datetime import datetime
now = datetime.now()
print(sys.argv)

def get_year(year):
  try:
    year = int(year)
    return year
  except ValueError:
    return 'Please enter a valid year!'
  
def get_month(mon):
  switcher = {
    "january": 1,
    "february": 2,
    "march": 3,
    "april": 4,
    "may": 5,
    "june": 6,
    "july": 7,
    "august": 8,
    "september": 9,
    "october": 10,
    "november": 11,
    "december": 12,
  }
  return switcher.get(mon.lower(), "Invalid Argument")

if len(sys.argv) == 1:
  print(calendar.month(now.year, now.month))
elif len(sys.argv) == 2:
  month = get_month(sys.argv[1])
  if month == "Invalid Argument":
    print('Please provide the month as the full string (ie. January, February) or as an integer (1, 2)')
  else:
    print(calendar.month(now.year, month))
elif len(sys.argv) == 3:
  month = get_month(sys.argv[1])
  year = get_year(sys.argv[2])
  if month == "Invalid Argument":
    print('Please provide the month as the full string (ie. January, February) or as an integer (1, 2)')
  elif year == 'Please enter a valid year!':
    print('Please enter year as a valid integer!')
  else:
    print(calendar.month(year, month))
else:
  print('Please run file correctly- "python3 14_cal.py [month] [year]"')