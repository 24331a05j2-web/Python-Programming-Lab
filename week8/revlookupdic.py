print("Reverse Lookup for Dictonary:")
dct={1:"Pen",2:"Pencil",3:"Paper",4:"Book",5:"Ink",6:"Eraser"}
print("The dictonary is:",dct)
dct1={v:k for k,v in dct.items()}
print(dct1)
value=input("Enter the value to find the key:")
if value in dct1:
    print("The key of the value is:", dct1[value])
else:
    print("Value not found in dictionary.")