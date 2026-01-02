import numpy as np

arr=np.array([[1,2,3],[4,5,6]])

print("The elements in the array is: ")
print(arr)
print("The shape or the dimension of the array is:",arr.shape)
print("The size of the array is: ",arr.size)
print("The transpose of the default matrix is: ")
print(arr.T)
print("The sum of all the elements in the array is:",np.sum(arr))
print("The sum of the elements in axis 0 is : ",np.sum(arr,axis=0)) # axis 0 is vertically supporting addition, so the elements of the same column are added
print("The sum of the elements in axis 1 is: ",np.sum(arr,axis=1)) # axis 1 is horizontally supporting addition, so the elements of the same row are added
print("The mean of the elements in the array: ",np.mean(arr))
print("The standard deviation of the mean is: ",np.std(arr))