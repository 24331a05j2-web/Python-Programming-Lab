import numpy as np
n=int(input("Enter number of elements: "))
data=[]
for i in range(n):
    print("Enter data for element number(",i,"): ",end="")
    data.append(int(input()))
arr=np.array(data)
print("")
print("The entire array of elements are: ",arr)
print("The first element of the array is: ",arr[0])
print("The last element of the array is: ",arr[-1])
print("Printing the sliced array of elements: ",arr[1:4]) #from index 1 to 3 as 1 is inclusive and 4 is exclusive
print("Adding 5 to each element of the array: ",arr+5)
print("Multiplying each element of the array with 2: ",arr*2)
print("Printing elements in the array which are greater than 25 : ",arr[arr>25])