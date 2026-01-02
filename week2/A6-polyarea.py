from math import pi,tan
print("Polygon Area Calculator:")
sidenum=int(input("Enter the number of sides of polygon: "))
sidelen=float(input("Enter the side lenght of the polygon: "))
area=(sidenum*(sidelen**2))/4*(tan(pi/sidenum))
print("The area of the polygon with the given parameters: ",round(area,2))