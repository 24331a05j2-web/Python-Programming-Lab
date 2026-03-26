print("Palindrome Authenticator")
string=input("Enter a string or number to see if it is a pallindrome: ")
result=string[::-1]

if string==result:
    print(string," is a palindrome")
else:
    print(string, "is not a palindrome")
