print("Create List of Tuples with Number and its Square")
lst=[]
n=int(input("Enter how many numbers you want: "))
for i in range(1,n+1):
    lst.append((i,i*i))
print("The list of tuples is:",lst)