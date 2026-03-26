print("Reverse number generator:")
number=int(input("Enter a number to reverse it: "))
num=int(number)
reversednumber=int(0)

while num>0 :
    temp=int(num%10)
    num=int(num/10)
    reversednumber=((reversednumber*10)+temp)
    
print(reversednumber," is the reversed number of ",number)
