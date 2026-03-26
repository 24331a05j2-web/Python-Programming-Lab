import math
radius=float(input("Enter radius of the Circle: "))
area= math.pi*radius*radius
print("The Area of the circle: ", round(area,2))

square=float(input("\nEnter the Number whose Square root is to be evaluated: "))
squareroot=math.sqrt(square)
print("The Square root the given number is: ",squareroot)

angle=float(input("\nEnter angle in degree: "))

print("The sin of the given angle is: ",round(math.sin(math.radians(angle)),4))
print("The cos of the given angle is: ",round(math.cos(math.radians(angle)),4))