def checker(number, checkval):
    global count
    if checkval == 0:
        return
    if number % checkval == 0:
        count += 1
    checker(number, checkval - 1)
print("Prime number checker:")
number = int(input("Enter a number to check if it's prime number: "))
count = 0
checker(number, number)
if count == 2:
    print("The given number is prime")
else:
    print("The given number isn't prime")
