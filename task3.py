#! python3

# Solve a two step algebra equation.
# Two steps equations are in the format ax + b = c
# You will ask the user to enter in all 3 variables: a, b and c
# You will need to display the solution for the equation

# inputs
# a, b, c
#
# outputs
# solution for x
#
# test case: 5, 1, 11 should give x = 2

a=int(input("Enter any num1: "))
b=int(input("Enter any num2: "))
c=int(input("Enter any num3: "))
print("3 numbers:", a, b, c)
x=(c-b)/a
print("Output: x =",int(x))
