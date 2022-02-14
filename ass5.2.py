#find out if a given year is a leap year or not
year=int(input("Enter year to be checked:"))
if(year%4==0 and year%100!=0 or year%400==0):
    print("The year is a leap year")
else:
    print("The year is not  a leap year")
2