print("Sum of elements in a list calculator:")
try:
    size=int(input("Enter the size of the list:"))
    lst=[]
    sum=0
    for _ in range(0,size):
        print("Enter element for",_+1,"element:",end="")
        temp=int(input())
        lst.append(temp)
        sum+=temp
    print("The sum of all the numbers in the list is:",sum)
except ValueError:
    print("Enter numbers only please.")
except:
    print("Run Time Error- Program Terminated")