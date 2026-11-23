""" Nom: Danut Marian Frincu
Implementa un control d'accés a una atracció.  
Genera totes les dades aleatòriament: l'alçada (entre 100cm i 210cm, l'edat (entre 10 i 25 anys) i si vol fotos (cert o fals). 
Ha de seguir el diagrama de flux. Has d'informar si pot pujar a l'atracció o no, i en cas que si en funció de l'edat i si volen fotos 
o no has cobrar un preu o un altre."""

import random
#el randint et genera soposo que un int random entre els numeros que es posin, 100, 210 en aquest cas
alcada = random.randint(100, 210)
#el random choice et fa una eleccio aleatoria entre els valors de dins del () en aquest cas pot ser o True o False
vols_fotos = random.choice([True,False])
#He posat una edat random entre 10 i 25
edat = random.randint(10, 25)
# una variable per comptar el total que s'ha de pagar
total_pagar = 0

#comprovacio d'altura, si es menys de 120 es massa baix i per tant no pot pujar
if (alcada <= 120):
    print("No pots pujar")

#comprovacio d'edat, si es menor de 12 paga 5
elif (edat < 12):
    print("Pues te va a costar 5$")
    total_pagar += 5

#comprovacio d'edat, si es major d'edat paga 12
elif (edat >= 18):
    print("Pues te va a costar 12$")
    total_pagar += 12

#comprovacio d'edat si esta entre 12 i 18 paga 7
elif (edat >= 12 and edat <= 18):
    print("Pues te va a costar 7$")
    total_pagar += 7
#comprovacio de fotos, nomes comprovo el True perque es el que paga, si el random choice dona False pues nada 
elif (vols_fotos == True):
    print("Pues te va a costar 3$")
    total_pagar += 3

#imprimo el total a pagar que sera la suma de la tria dels anteriors ifs.
print(total_pagar)




    