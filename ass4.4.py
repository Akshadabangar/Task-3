#WAP to demonstrate use of logical operators

# Python program to demonstrate
# logical and operator

a = 45
b = -25
c = 56

if a > 0 and b > 0:
    print("The numbers are greater than 0")

if a > 0 and b > 0 and c > 0:
    print("The numbers are greater than 0")
else:
    print("Atleast one number is not greater than 0")

    str1 = "Hello "
    str2= "world"
    print(repr(str1 and str2))
    print(repr(str2 and str1))
    print(repr(str1 or str2))
    print(repr(str2 or str1))
    print(repr(not str1))