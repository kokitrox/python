##oscar avila 5to BIPC
## selccionar una opccion y trabajar potencia
print ("1.opccion 2.opccion".center(50,"-"))
opccion = input (":.") 
if  opccion == "1":
    numero1 = input("ingrese un valor")
    numero2 = input("ingrese otro valor")
    potenciacion = int(numero1) ** int(numero2)
    print("la potenciacion es:. {}".format(potenciacion))
elif  opccion == "2":
    numero1 = input("ingrese un valor")
    numero2 = input("ingrese otro valor")
    numero3 = input("ingrece tercer numero")
    potenciacion = int(numero1) ** int(numero2) ** int(numero3)
    print("la potenciacion es:. {}".format(potenciacion))
else:
    print("opccion no valida")

