'''Calcula la potència n d’un nombre sencer utilitzant recursivitat.'''

def potencia(base, exponente):
    # Si el exponente es 0, devuelve 1
    if exponente == 0:
        return 1
    # Si el exponente es 1, devuelve la base
    elif exponente == 1:
        return base
    # Si el exponente es mayor que 1, llama de nuevo a la función restando 1 al exponente
    else:
        return base * potencia(base, exponente - 1)
    
print(potencia(3,4))