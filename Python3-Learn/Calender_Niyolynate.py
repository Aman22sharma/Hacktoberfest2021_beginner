# AUTHOR: Niyo Lynate
# Python3 Concept: A Calender program that displays one month
# GITHUB: https://github.com/niyolynate

# Python program to display calendar of given month of the year

# import module
import calendar

# To ask month and year from the user
yy = int(input("Enter year: "))
mm = int(input("Enter month: "))

# display the calendar
print(calendar.month(yy, mm))