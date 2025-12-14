numint=int(input("Enter a Integer Number: "))
numfloat=float(input("Enter a Floating point number: "))
result=numint+numfloat
print("\nImplicit type conversion:\nThe sum of Both the above numbers : ",round(result,3))
print("Type of the result: ",type(result))

numfloat=float(input("\nEnter a Floating point number: "))
result=int(numfloat)
print("\nExplicit type conversion:\nThe Number after explicit type conversion :",result)

print("Type of result: ",type(result))
print("\n")

print("Type of result: ",type(result))