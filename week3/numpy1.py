import numpy as np
n=int(input("Enter number of elements: "))
data=[]
for i in range(n):
    print("Enter data for element number(",i,"): ",end="")
    data.append(int(input()))
print("")
arr=np.array(data)
print("Printing the entire array of elements: ",arr)
print("Sum of the elements in the array is: ",np.sum(arr))
print("Mean of the elements in the array is: ",np.mean(arr))
print("The max element in the array is: ",np.max(arr))
print("The min element in the array is: ",np.min(arr))