def fibo(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
number=int(input("Enter the number of fibonacci series you want to see: "))
if number<0:
    print("The number of terms cant be negative!, So the program is terminated")
else:
    print("The fibonacci series is: ")
    for i in range(1,number+1):
        print(fibo(i),end=" ")