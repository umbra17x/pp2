#Example1(Import the datetime module and display the current date)
import datetime
x = datetime.datetime.now()
print(x)
#Example2(Return the year and name of weekday)
import datetime
x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))
#Example3(Create a data object)
import datetime
x = datetime.datetime(2020, 5,17)
print(x)
#Example4(display the name of the month)
import datetime
x = datetime.datetime(2018,6,1)
print(x.strftime("%B"))