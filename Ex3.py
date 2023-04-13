'''Fes una funció recursiva per girar un string'''

def gira_string(s):
    # Si la cadena es vacía o mide 1, devuelve la cadena
    if len(s) <= 1:
        return s
    # Devuelve la última letra de la cadena seguida del resultado llamar a la función con la cadena menos la última letra.
    else:
        return s[-1] + gira_string(s[:-1])
    
print(gira_string('El gato con botas'))