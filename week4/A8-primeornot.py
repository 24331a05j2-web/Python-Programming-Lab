print("Prime number checker:")
n=int(input("Enter a number to check if it's a prime number: "))
if n <= 1:
    print("Not Prime")
else:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")