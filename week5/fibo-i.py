print("Fibonacci series generator:")
number=int(input("Enter the number of terms of fibonacci series to be see: "))
oldval=0
newval=1
for i in range(1,number+1):
    print(oldval,end=" ")
    temp=oldval
    oldval=newval
    newval=newval+temp
print()