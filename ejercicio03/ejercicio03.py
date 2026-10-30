# Ejercicio 3: Envíos de la juguetería
numero_payasos = int(input("¿Cuántos payasos se han vendido?: "))
numero_munecas = int(input("¿Cuántas muñecas se han vendido?: "))
precio_gramo = float(input("Introduce el precio de envío por gramo: "))

peso_total = (numero_payasos * 112) + (numero_munecas * 75)
coste_envio = peso_total * precio_gramo

print(f"El peso total del paquete es de {peso_total} gramos.")
print(f"El coste total del envío será de {coste_envio} euros.")