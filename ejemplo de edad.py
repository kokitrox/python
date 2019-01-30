## oscar avila 5to BIPC
## calcula la edad actual de una persona
## previamente ingresando
## año actual y el nacimiento
print ("bienvendio al programa".center(50,"*"))
FEC_ACT= 2019
fech_nac = int(input("ingrese la anio de nacimiento"))

edad = FEC_ACT - fech_nac

print("tu edad es {}".format(edad))
if edad >= 18:
    print("eres mayor de edad")
else:
    print("eres menor de edad")
