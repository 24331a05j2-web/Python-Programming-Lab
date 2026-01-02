def GCD(a,b):
    if b==0:
        return a
    else:
        return GCD(b,a%b)
print("GCD Calculator:")
number1=int(input("Enter the first number: "))
number2=int(input("Enter the second number: "))

print("The GCD of ",number1," and ",number2," is: ",GCD(number1,number2))
