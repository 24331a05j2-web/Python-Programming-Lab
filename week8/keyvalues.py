print("Add to or modify the Dictonary:")
dct={}
try:
    while(1):
        print("Select an option:\n1.Modify existing Dictonary values\n2.Add new pair to Dictonary\n3.View Dictonary\n4.Exit\nEnter an option:",end="")
        choice=int(input())
        if(choice==1):
            keyitem=input("Enter the key value to modify its values:")
            valmod=input("Enter the value to replace the existing value at Key:")
            dct[keyitem]=valmod
            print("The modified dictonary is:",dct)
        elif(choice==2):
            keyitem=input("Enter a new key value:")
            valitem=input("Enter a Value for the key:")
            dct[keyitem]=valitem
        elif(choice==3):
            print("The Dictonary is:",dct)
        elif(choice==4):
            print("Program Terminated.")
            exit()
        else:
            print("Invalid Option. Please enter a valid option")    
except:
    print("Invalid Input. Program Terminated")        