def passinglist(lst):
    print(lst)
print("Passing list as argument:")
try:
    number=int(input("Enter the number of terms you want to enter into the list:"))
    lst=[]
    for _ in range(0,number):
        temp=int(input("Enter the term: "))
        lst.append(temp)
    passinglist(lst)
except ValueError:
    print("Enter numbers only")