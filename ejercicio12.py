cont=0
num=0
a=int(input("ingrese un número: "))
while num<=a:
    num+=1
    if a % num==0:
        cont+=1
if cont==2:
        print("númwero primo")
else:
    print("No primo")

