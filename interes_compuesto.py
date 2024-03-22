# Programa para calcular el interes compuesto de un monto de dinero en 12 meses

# input

C = int(input("Ingrese el capital inicial entregado: "))

# Processing 
N = 0
D = 2 * C

while (C <= D):
    C = 1.05 * C
    N= N + 1

# output

print("Su capital inicial fue de", D/2 ,)
print("El dinero dado al banco ya duplico su valor, este es el monto actual", C ,)
print("El dinero demoro ", N ,"meses para llegar a este valor")