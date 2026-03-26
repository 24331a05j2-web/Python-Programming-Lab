print("Prime value checker:")
number=int(input("Enter the number to check if it's a prime number: "))
count=0
if number<1 :
    print("Only positive numbers can be acceepted as input!\nProgram  terminated")  
else:
    for i in range(1,number+1):
        if number%i==0 :
            count+=1
        if count>2 :
            break
    if count<=2 :
        print("The given number is a prime number")
    else:
        print("The given number is not a prime number")