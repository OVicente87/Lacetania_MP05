'''Fes una funció per sumar tots els elements d’una llista.'''

def suma_recursiva(lista):
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + suma_recursiva(lista[1:])
    
lista = [10,20,30,40]

print(suma_recursiva(lista))

lista = [10,20,30,40,50]

print(suma_recursiva(lista))
