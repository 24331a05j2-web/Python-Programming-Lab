tupl=()
tupl1=(0,1,2,3,4,5,6,7,8,9)
tupl2=tuple(x for x in tupl1)
print(tupl2)

dct={1:"Pen",2:"Pencil",3:"Paper",4:"Book",5:"Ink",6:"Eraser"}
dct2={k:v for k,v in dct.items()}
print(dct2)