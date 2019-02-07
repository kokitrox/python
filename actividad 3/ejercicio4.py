## ejercicio 4
## oscar ely avila lopez
## realizar promedio d en notas
n = 0
suma = 0
print("bienvenidos al programa:) ".center(50,"-"))

print ("ingresa las notas que deceas, ingrese 1 para detener el programa")

cantidad = int(input("ingresa la cantidad de notas que podras:. "))
for i in range(cantidad):
    n = int(input("ingrese notas :."))
    suma = suma + n
    promedio = suma / cantidad
    print(" el promedio es:. {}".format(promedio))
                     

