def aniobisiestro():
    anio: int = int (input("Introduce el Año y para verificar si es bisiestro :   "))

    if (anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)):
        print("el anio ha sido verificado,",anio,"es bisiestro")

    else: 
        print("ha sido verificado, EL año ", anio, "no es bisiestro")


print(aniobisiestro())
