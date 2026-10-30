n1= int(input("Dime un nummero entero: "))
n2= int(input("Dime un numero entero: "))
conteo=0

while n1>= n2:
    print("Error")
    
    n1= int(input("Dime un nummero entero: "))
    n2= int(input("Dime un numero entero: "))
    
for suma in range(n1,n2+1):
    conteo+=suma
print(f"{conteo}")
