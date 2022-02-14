#Accept the month number and print its name and number of days in it
print(
    "List of months: January, February, March, April, May, June, July, August, September, October, November, December")
month_name = input("Input the name of Month: ")
month_num=input("Input the num of month:")
if month_name == "February":
    month_num="2"
    print("No. of days: 28/29 days")
elif month_name in ("April", "June", "September", "November"):
    month_num="4","6","9","11"
    print("No. of days: 30 days")
elif month_name in ("January", "March", "May", "July", "August", "October", "December"):
    month_num="1","3","5","7","8","10","12"
    print("No. of days: 31 day")
else:
    print("Wrong month name")
