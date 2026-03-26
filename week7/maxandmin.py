print("Max and Min in a list:")
try:
    size=int(input("Enter the size of the list:"))
    lst=[]
    for _ in range(0,size):
        print("Enter element for",_+1,"element:",end="")
        temp=int(input())
        lst.append(temp)
    max=min=lst[0]
    for _ in range(0,size):
        if(max<lst[_]):
            max=lst[_]
        if(min>lst[_]):
            min=lst[_]
    print("The largest element in the list is:",max)
    print("The smallest element in the list is:",min)
except ValueError:
    print("Enter numbers only. please.")
except:
    print("Runtime Error- Program Terminated")