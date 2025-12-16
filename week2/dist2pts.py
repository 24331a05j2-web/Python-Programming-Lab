from math import sqrt
print("Distance between 2 points Calculator:")
x1=int(input("Enter the X-coordinate of the 1st point: "))
y1=int(input("Enter the Y-coordinate of the 1st point: "))
x2=int(input("Enter the X-coordinate of the 2st point: "))
y2=int(input("Enter the Y-coordinate of the 2st point: "))
dist=sqrt((x2-x1)**2 + (y2-y1)**2)
print("The distance between the given points is: ",round(dist,2))