import math

p , b = int(input()),int(input())

#The arctan function is the inverse of the tangent function
c = str(round(math.degrees(math.atan2(p , b)))) + '°'

print(c)
