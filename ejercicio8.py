suma=0
numero=0
a=int(input("ingrese un valor: "))
for i in range(1, a):
    if a % i==0:
       print(i) 
if suma==a:
    print("No perfecto")
    
else: 
    print(" PERFECTO")     