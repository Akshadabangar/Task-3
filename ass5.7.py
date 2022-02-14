#WAP to check if a candidate is eligible to vote or not
age = int(input("Enter Age : "))
if age>=18:
        status="Eligible"
else:
    status="Not Eligible"

print("You are ",status," for Vote.")

