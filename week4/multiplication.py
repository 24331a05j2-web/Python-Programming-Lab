print("Multiplication table: ")
number=int(input("Enter the number of what table you want to display: "))
print("The multiplication table of ",number," is:")
for i in range(1,13):
    print(number,"*",i,"=",number*i)
