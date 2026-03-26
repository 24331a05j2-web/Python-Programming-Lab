print("Armstrong number checker:")
number=int(input("Enter a number to check if it's an armstrong number:"))
count=int(len(str(number)))
sum=int(0)
num=str(number)
for i in range(count):
    sum+=(int(num[i]))**count

if sum==number :
    print(number," is an armstrong number")
else:
    print(number," isnt an armstrong number")