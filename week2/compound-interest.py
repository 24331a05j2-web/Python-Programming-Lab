print("Compound Interest Calculation:")
principle=float(input("Enter the principle amount: "))
rate=float(input("Enter the rate of interest: "))
time=float(input("Enter the time(in years): "))
ci=(principle*(1+(rate/100))**time)-principle
print("The Compound Interest for the given values is ",ci)