#! python3
#
# Find the radius of a sphere if you are given the volume.
# Think about how you would need to solve this equation if you were doing it on paper
#
# Inputs:
# Volume (float)
#
# Outputs:
# radius (float)
#
# Test output Volume of 20.22 should give radius of:1.69002229118
# Note: You will need to do some strange things with your cube root.
# Remember that a cube root is the same as an exponent of 1/3, but
# here you will need to do a power of 1.0/3 or something strange happens.
import math
V=float(input("Enter the volume of sphere: "))
print("Volume of sphere: ",V)
rad3=V*(3/4)/math.pi
rad=math.pow(rad3,1.0/3)
print("radius of the sphere is ",rad)
