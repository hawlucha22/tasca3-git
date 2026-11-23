""" Nom: Danut Marian Frincu
Fes un programa que donat un número sencer que introduïm per teclat ens digui si és parell o és senar, i també si és positiu o negatiu:
	
	Per l'entrada 5 mostrarà per consola:

	* El número 5 és senar i positiu
"""



numero = int(input("Introdueix el numero per teclat: "))

# amb la operacio de % 2 == 0 m'aseguro que qualsevol multiple de 2 sigui parell, i si es 0 o > que sigui positiu
if (numero % 2 == 0 and numero >= 0):
    print(f"El número {numero} és parell i positiu")

# el mateix per els parells pero amb numeros negatius
elif (numero % 2 == 0 and numero < 0):
    print(f"El número {numero} és parell i negatiu")

#un else perque ara comprovare els senars, i el mateix he fet, si no es multiple de 2 es senar. i positiu-negatiu el mateix que a dalt
else: 
    if (numero % 2 != 0 and numero >= 0):
        print(f"El número {numero} és senar i positiu")
    else:
        print(f"El número {numero} és senar i negatiu")

