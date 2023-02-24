#! python3
"""
Ask the user for their name and their email address.
(2 points)

Inputs:
 name
 email

Sample output:
 Your name is Joe Lunchbox, and your email is joe@koolsandwiches.org.
"""
x = str( input("Enter your name: "))
print("name: " + x)
y = str(input("Enter your email: "))
print("email: " + y)
print ("Your name is" +x +", and your eamil is " +y)