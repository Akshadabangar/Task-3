#Write a program to calculate simple interest accept value from user
p = float(input("Enter the principal amount : "))

n = float(input("Enter the number of years : "))

r = float(input("Enter the rate of interest : "))

# calculate simple interest by using this formula
Si = (p*n*r) / 100

# print
print("Simple interest : {}".format(Si))
