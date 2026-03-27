from random import randint
file=open("Textfile.txt","w+")
for _ in range(0,20):
    temp=randint(1,101)
    file.writelines(str(temp)+"\n")
file.close()
print("Done")