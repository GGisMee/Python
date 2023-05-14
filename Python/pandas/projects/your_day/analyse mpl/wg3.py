from datetime import datetime 
import calendar
year = datetime.now().year
month = datetime.now().month
cal = calendar.monthcalendar(year, month)
print(cal)