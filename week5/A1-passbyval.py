def incrementer(val):
    val+=10
    return val
print("Pass by value demonstration:")
value=int(input("Enter a number to increment it by 10: "))
print("The value before function call: ",value)
print("The value in function call(passing val and modifying it): ",incrementer(value))
print("The value after function call: ",value)