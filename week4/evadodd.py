print("Even and odd digit counter:")
number=int(input("Enter the number till where you want to count(starts from 1): "))
evecount=0
oddcount=0
for i in range(1,number+1):
    if i%2==0 :
        evecount+=1
    elif i%2!=0 :
        oddcount+=1

print("The number of even numbers in the given range is: ",evecount)
print("The number of odd numbers in the given range is: ",oddcount)
