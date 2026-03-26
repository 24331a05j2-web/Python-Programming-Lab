print("Dictonary methods:")
dct={1:"Pen",2:"Pencil",3:"Paper",4:"Book",5:"Ink",6:"Eraser"}
print("The data present in the dictonary is:",dct)
print("The Key of the dictonary is:",dct.keys())
print("The Values of the dictonary is:",dct.values())
print("The total items in the dictonary is:",dct.items())
dct.pop(6)
print("After popping a pair, the dictonary is:",dct)
if 5 in dct:
    del dct[5]