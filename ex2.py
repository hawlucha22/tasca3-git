""" Nom: Danut Marian Frincu
Escriviu un programa Python per comprovar si un nombre que introduïm per teclat és múltiple de 7 i múltiple de 5 a la vegada."""

numero = int(input("Introdueix el numero: "))

#amb la operacio de modul qualsevol numero % == 0 comprovem el seu multiple per tant nomes tenia que posar el and per a que siguen els 2 a la vegada
if (numero % 7 == 0 and numero % 5 == 0):
    print("Efectivament aquest numero si es múltiple de 7 i 5 a la vegada")
else:
    print("NO es multiple de 7 i 5 a la vegada.")
    
#i el else per qualsevol numero q no es multiple de 7 i 5 a la vegada