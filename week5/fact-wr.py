def fact(n):
    factorial=1
    if n==0:
        return 1
    else:
        return n*fact(n-1)

print("Factorial calculator with recursion:")
value=int(input("Enter the number to calculate factorial:"))
if value<0 :
    print("Factorial cant be calculated for negative numbers.\nProgram terminated")
else:
    factorial=fact(value)
    print("The factorial of",value,"is",factorial)