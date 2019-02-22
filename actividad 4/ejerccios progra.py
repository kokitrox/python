##1.
##PRESTAMO = 10000
##DESCUENTO = 0.27
##interes = 0
##print("Bienvenidos al programa")
##interes = PRESTAMO * DESCUENTO
##print("el interes a pagar anual es:{}".format (interes))

##2
##KILOMETRO = 10.50
##costo = 0
##km =int(input("ingrese kilometros a recorrer:"))
##costo = km * KILOMETRO
##print("el total  por los boletos es de:{}".format(costo))

##3
##HORA = 1.5
##costo = 0
##horas = int(input("ingrese cuanto tiempo necesita la cabina de internet:"))
##if horas <= 4:
##    costo = horas * HORA
##    print("el costo a pagar es de:{}".format(costo))
##if horas >= 5:
##        costo = horas * HORA
##        print("el costo a pagar es de:{}".format(costo))
##        print("tienes una hora extra")

##4.
##DOLAR = 2.15
##EUROS = 1.45
##dolares = 0
##euros = 0
##menu = int(input("1.dolares a euros 2.Euros a dolares"))
##if menu == 1:
##    dolares = int(input("ingrese cantidad de dolares"))
##    cambio = dolares / EUROS
##    print("el cambio a euros es de:{}".format(cambio))
##elif menu == 2:
##    euros = int(input("ingrese cantidad de dolares"))
##    cambio = euros * DOLAR
##    print("el cambio a dolares es de:{}".format(cambio))
##else:
##    print("operacion erronea")


##5.
##DESCUENTO = 0.35
##descuento = 0
##total = 0
##medicamento = int(input("ingrese el costo de la medicina:"))
##descuento = medicamento * DESCUENTO
##total = medicamento - descuento
##print("el descento es de:{}".format(descuento))
##print("el total a pagar es de:{}".format(total))

##6.
##INCREMENTO = 0.8
##DESCUENTO = 0.025
##sueldo = int(input("ingrese sueldo actual:"))
##aumento = sueldo * INCREMENTO
##suma = sueldo + aumento
##descuento = suma * 0.025
##resta = suma - descuento
##print("el sueldo nuevo es de:{}".format(resta))


##7
##URGENCIA = 0.37
##PEDIATRIA = 0.42
##TRAUMATOLOGIA = 0.21
##print("Desea calcular presupuesto")
##salida = input("Ingresar presupuesto 1-si \n 2-no")
##while salida != 2:
##    presupuesto = int(input("Ingresar cantidad"))
##    print("La cantidad es:.{}".format(presupuesto * URGENCIA))
##    print("La cantidad es:.{}".format(presupuesto * PEDIATRIA))
##    print("La cantidad es:.{}".format(presupuesto * TRAUMATOLOGIA))
##    salida = input("Ingresar presupuesto 1-si \n 2-no")
##print ("Gracias")
##8
##CENT1 = 0.05
##CENT2 = 0.10
##CENT3 = 0.12
##CENT4 = 0.05
##CENT5 = 0.25
##CENT6 = 0.50
##BOLIVAR = 1
##suma = (CENT1 + CENT2 + CENT3 + CENT4 + CENT5 + CENT6 + BOLIVAR)
##print("la cantidad de dinero total es de:.{}".format(suma))
##

##9.
##va_h = 0
##h = 0
##h_e = 0
##valor_horas = int(input("Valor de las horas"))
##hora = int(input("Horas trabajadas"))
##hora_extra = int(input("Horas extras laboradas"))
##va_h = int(valor_horas)*int(hora) 
##h = int(valor_horas) * int(hora_extra)*int(2)
##h_e = int(valor_horas)+int(valor_horas)*int(hora_extra)*int(2)
##print("Su sueldo normal es:.{}".format(va_h))
##print("Su sueldo extra es:.{}".format(h))
##print("El total es:.{}".format(h_e))
##
##10.
ARENA = 0.5
largo = 0
alto = 0
largo = int(input("ingrese el largo de la pared"))
alto = int(input("ingrese el ancho de la pared"))
arena = (largo * alto) * 0.5
print("la cantidad de arena necesaria es de:{}".format(arena)) 

 
##11
##HORAS = 3600
##MINUTOS = 60
##SEGUNDOS = 0.25
##menu = int(input("1.tiempo en horas 2.tiempo en minutos 3.tiempo en segundos"))
##if menu == 1:
##    horas = int(input("ingrese cuantas horas necesita"))
##    tiempo = horas * HORAS
##    total = tiempo * SEGUNDOS
##    print("el total a pagar por el tiempo es de:{}".format(total))
##elif menu == 2:
##    minutos = int(input("ingrese cuantos minutos necesita"))
##    tiempo = minutos * MINUTOS
##    total = tiempo * SEGUNDOS
##    print("el total a pagar por el tiempo es de:{}".format(total))
##if menu == 3:
##    segundos = int(input("ingrese cuantos segundos necesita"))
##    total = segundos * SEGUNDOS
##    print("el total a pagar por el tiempo es de:{}".format(total))


##12.
##DESCUENTO = 0.20
##salario = 0
##salario = int(input("Ingrese su sueldo:"))
##descuento = salario * DESCUENTO
##resta = salario - descuento
##print("Su sueldo nuevo es de:{}".format(resta))

##13.
##n1 = 0
##n2 = 0
##n1 = int(input("ingrese primer numero"))
##n2 = int(input("ingrese segundo numero"))
##suma = n1 + n1
##elevacion = n2 ** 2
##total = suma + elevacion
##print("El total es de:{}".format(total))
##cubo = (n1 ** 3)+ (n2 ** 3)
##promedio = cubo / 2
##print("El promedio de sus cubos es de:{}".format(promedio))

##14.
##n1 = 0
##n2 = 0 
##n3 = 0
##lista = 0
##n1 = int(input("Ingrese primer numero:"))
##n2 = int(input("Ingrese segundo numero:"))
##n3 = int(input("Ingrese tercer numero:"))
##lista(n1,n2,3)

##15.
##anios = 0
##meses = 0
##anios = int(input("ingrese edad en anios:"))
##meses = int(input("ingrese meses despues del los anio"))
##mult = anios * 12
##suma = meses + mult
##print("total de sus meses:{}".format(suma))

##16
##PORCENTAJE = 0.025
##capital = 0
##capital = int(input("ingrese el capital a invertir:"))
##mult = capital *PORCENTAJE
##total = mult * 12
##print ("El dinero a ganar en un año es de:{}".format(total))

##17.
##sueldo = 0
##EXTRA = 0.10
##venta1 = 0
##venta2 = 0
##venta3 = 0
##sueldo = int(input("ingrese su sueldo base"))
##venta1 = int(input("ingrese cantidad de su venta"))
##venta2 = int(input("ingrese cantidad de su venta"))
##venta3 = int(input("ingrese cantidad de su venta"))
##suma = (venta1 + venta2 + venta3) * EXTRA
##total = sueldo + suma
##print ("pago de sus comisiones:{}".format(suma))
##print ("EL total de su sueldo es de:{}".format(total))

##18.
##DESCUENTO = 0.15
##compra = 0
##descuento = 0
##compra = int(input("ingrese el costo de su compra:"))
##descuento = compra * DESCUENTO
##total = compra - descuento
##print("su descuento es de:{}".format(descuento))
##print("El total a pagar es de:{}".format(total))



##19:
##nota1 = input("Ingrese nota")
##nota2 = input("Ingrese nota")
##nota3 = input("Ingrese nota")
##promedio = 0
##suma = 0
##suma = int(nota1) + int(nota2) + int(nota3) 
##print ("La calificacion final es:.{}".format(suma))

##20.
##PORCENTAJE = 0.100
##hombres = 0
##mujeres = 0
##hombres = int(input("ingrese cantidad de hombres"))
##mujeres = int(input("ingrese cantidad de mujeres"))
##porcentaje_h = hombres * PORCENTAJE
##porcentaje_m = mujeres * PORCENTAJE
##print("el porcentaje de hombres es de:{}".format(porcentaje_h))
##print("el porcentaje de muejeres es de:{}".format(porcentaje_m))

##21.
##INCREMENTO = 0.25
##salario = 0
##salario = int(input("ingrese su salario:"))
##salario_nuevo = salario * INCREMENTO
##suma = salario_nuevo + salario
##print ("Su saldo nuevo es de:{}".format(suma))

##22.
##PIES = 3.28
##PULGADAS = 39.37
##metros = 0
##metros = int(input("ingrese cuantos metros decea convertir:."))
##pies = metros * PIES
##pulgadas = metros * PULGADAS
##print("La distanci en Pies es de:.{}".format(pies))
##print("La distanci en Pulgadas es de:.{}".format(pulgadas))
##
##23.
##24.
##25:
##suma = 0
##multiplicacion = 0
##num1 = int(input("Ingrese numero1"))
##num2 = int(input("Ingrese numero2"))
##suma = int(num1) + int(num2)
##print("La suma es:.{}".format(suma))
##multiplicacion = int(num1) * int(num2)
##print("La multiplicacion es:.{}".format(multiplicacion))

##26:
##valor1 = int(input("Ingrese numero1"))
##valor2 = int(input("Ingrese numero2"))
##valor3 = int(input("Ingrese numero3"))
##suma = int(valor1) + int(valor2) + int(valor3)
##resta = int(valor1) - int(valor2) - int(valor3)
##multiplicacion = int(valor1) * int(valor2) * int(valor3)
##print ("La suma es:.{}".format(suma))
##print ("La resta es:.{}".format(resta))
##print ("La multiplicacion es:.{}".format(multiplicacion))

##27:
##nacimiento = int(input("Ingrese anio de nacimiento"))
##DATO2 = 2019
##edad = DATO2 - nacimiento
##print ("Tu edad es:.{}".format(edad))


