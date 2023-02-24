#! python3
#
# Surface area of a cone
# Find the surface area of a cone given the height and the radius.
# You will need to ask the user to enter in both variables, and will 
# need to use the Pythagorean relationship to find the slant height. 
# (2 points)
#
# Inputs:
# height, radius
#
# Outputs:
# surface area
#
# Test output
# r = 3
# h = 5
# sa = 83.2297607912
import math
h=int(input("Enter the height of cone: "))
r=int(input("enter the radius of cone: "))
print("height: ",h, "radius: ",r)
l=math.sqrt(math.pow(h,2)+math.pow(r,2))
surfaceArea=(math.pi*math.pow(r,2))+(math.pi*r*l)
print("surfaceArea of cone: ", surfaceArea)