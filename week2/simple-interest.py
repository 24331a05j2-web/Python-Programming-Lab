print("Simple Interest Calculation:")
principle=float(input("Enter the principle amount: "))
rate=float(input("Enter the rate of interest: "))
time=int(input("Enter the time(in years): "))
si=(principle*rate*time)/100
print("The simple interest with the given data: ",si)