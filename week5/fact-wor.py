def fact(n):
    factorial=1
    for _ in range(2,n+1):
        factorial*= _
    return factorial
print("Factorial calculator with recursion:")
value=int(input("Enter the number to calculate factorial:"))
if value<0 :
    print("Factorial cant be calculated for negative numbers.\nProgram terminated")
else:
    factorial=fact(value)
    print("The factorial of",value,"is",factorial)